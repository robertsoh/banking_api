from rest_framework import serializers
from banking.accounts.factories import create_bank_account_interactor, create_bank_account_repository
from banking.common.models import EntityDoesNotExistException
from banking.customers.factories import create_customer_repository


class BankAccountSerialize(serializers.Serializer):
    number = serializers.CharField(max_length=20)
    balance = serializers.DecimalField(max_digits=14, decimal_places=2, allow_null=True)
    isLocked = serializers.BooleanField(default=True)
    customer_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_bank_account_interactor = create_bank_account_interactor()
        self.customer_repository = create_customer_repository()
        self.bank_account_repository = create_bank_account_repository()

    @staticmethod
    def to_dict(account):
        return {
            'id': account.id,
            'number': account.number,
            'balance': account.balance,
            'customer_id': account.customer_id,
            'isLocked': account.is_locked
        }

    def validate_customer_id(self, value):
        try:
            self.customer_repository.get_customer_by_id(value)
            return value
        except EntityDoesNotExistException as ex:
            raise serializers.ValidationError(ex.get_message())

    def validate_number(self, value):
        if self.bank_account_repository.exists_account_number(value):
            raise serializers.ValidationError('Account number already exists')
        return value

    def create(self, validated_data):
        account = self.create_bank_account_interactor.set_params(
            number=validated_data.get('number'),
            balance=validated_data.get('balance'),
            is_locked=validated_data.get('isLocked'),
            customer_id=validated_data.get('customer_id')
        ).execute()
        return self.to_dict(account)

    def update(self, instance, validated_data):
        super(BankAccountSerialize, self).update()
