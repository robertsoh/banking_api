from banking.customers.entities import Customer


class CreateCustomerInteractor(object):

    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def set_params(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        return self

    def execute(self):
        customer = Customer(first_name=self.first_name, last_name=self.last_name)
        return self.customer_repository.create(customer)
