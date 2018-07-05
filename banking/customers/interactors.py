from banking.customers.entities import Customer


class CreateCustomerInteractor:

    def __init__(self, customer_repository, customer_validator):
        self.customer_repository = customer_repository
        self.customer_validator = customer_validator

    def set_params(self, first_name, last_name, document_number):
        self.first_name = first_name
        self.last_name = last_name
        self.document_number = document_number
        return self

    def execute(self):
        customer = Customer(first_name=self.first_name,
                            last_name=self.last_name,
                            document_number=self.document_number)
        self.customer_validator.validate(customer)
        return self.customer_repository.create(customer)
