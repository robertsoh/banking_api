from rest_framework import serializers
from banking.accounts.factories import create_bank_account_interactor


class BankAccountSerialize(serializers.Serializer):
    number = serializers.CharField(max_length=20)
    balance = serializers.DecimalField(max_digits=14, decimal_places=2, allow_null=True)
    isLocked = serializers.BooleanField(default=True)
    customer_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_bank_account_interactor = create_bank_account_interactor()

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
        if value > 10:
            raise serializers.ValidationError('Does not exist')
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
        pass
