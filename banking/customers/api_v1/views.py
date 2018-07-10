from banking.common.decorators import serialize_exceptions
from banking.customers.api_v1.serializers import CustomerSerializer, CustomersSerializer


class CustomerListCreateView:

    def __init__(self, create_customer_interactor=None,
                 get_all_customers_interactor=None):
        self.create_customer_interactor = create_customer_interactor
        self.get_all_customers_interactor = get_all_customers_interactor

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

    @serialize_exceptions
    def get(self):
        customers = self.get_all_customers_interactor.execute()
        body = CustomersSerializer.serialize(customers)
        status = 200
        return body, status


class CustomerRetrieveUpdateDeleteView:

    def __init__(self,
                 get_customer_interactor=None,
                 update_customer_interactor=None,
                 delete_customer_interactor=None):
        self.get_customer_interactor = get_customer_interactor
        self.update_customer_interactor = update_customer_interactor
        self.delete_customer_interactor = delete_customer_interactor

    @serialize_exceptions
    def get(self, customer_id):
        customer = self.get_customer_interactor.set_params(id=customer_id).execute()
        body = CustomerSerializer.serialize(customer)
        status = 200
        return body, status

    @serialize_exceptions
    def patch(self, data):
        customer = self.update_customer_interactor.set_params(
            id=data.get('customer_id'),
            first_name=data.get('firstName'),
            last_name=data.get('lastName'),
            document_number=data.get('documentNumber')
        ).execute()
        body = CustomerSerializer.serialize(customer)
        status = 200
        return body, status

    @serialize_exceptions
    def delete(self, customer_id):
        self.delete_customer_interactor.set_params(id=customer_id).execute()
        body = None
        status = 204
        return body, status
