from rest_framework import serializers

from banking.customers.factories import create_customer_interactor, create_customer_repository


class CustomerSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)
    documentNumber = serializers.CharField(max_length=15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_customer_interactor = create_customer_interactor()
        self.customer_repository = create_customer_repository()

    def to_dict_customer(self, customer):
        return {
            'id': customer.id,
            'firstName': customer.first_name,
            'lastName': customer.last_name,
            'documentNumber': customer.document_number
        }

    def validate_documentNumber(self, value):
        if self.customer_repository.exists_document_number(value):
            raise serializers.ValidationError('Document number already exists')
        return value

    def create(self, validated_data):
        customer = self.create_customer_interactor.set_params(
            first_name=validated_data.get('firstName'),
            last_name=validated_data.get('lastName'),
            document_number=validated_data.get('documentNumber')
        ).execute()
        return self.to_dict_customer(customer)

    def update(self, instance, validated_data):
        super().update()

    def to_dict_customers(self, customers):
        return [self.to_dict_customer(customer) for customer in customers]
