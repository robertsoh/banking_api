from banking.customers.api_v1.serializers import CustomerSerializer


class CustomerView:

    def __init__(self, create_customer_interactor):
        self.create_customer_interactor = create_customer_interactor

    def post(self, firstName, lastName):
        customer = self.create_customer_interactor.set_params(first_name=firstName,
                                                              last_name=lastName).execute()
        body = CustomerSerializer.serialize(customer)
        status = 201
        return body, status
