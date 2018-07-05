from banking.common.decorators import serialize_exceptions
from banking.customers.api_v1.serializers import CustomerSerializer


class CustomerView:

    def __init__(self, create_customer_interactor=None):
        self.create_customer_interactor = create_customer_interactor

    @serialize_exceptions
    def post(self, data):
        customer = self.create_customer_interactor.set_params(
            first_name=data.get('firstName'),
            last_name=data.get('lastName'),
            document_number=data.get('documentNumber')
        ).execute()
        body = CustomerSerializer.serialize(customer)
        status = 201
        return body, status
