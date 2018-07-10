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


class GetCustomerInteractor:

    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.customer_repository.get_customer_by_id(self.id)


class GetAllCustomersInteractor:

    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def execute(self):
        return self.customer_repository.get_all_customers()


class UpdateCustomerInteractor:

    def __init__(self, customer_repository, customer_validator):
        self.customer_repository = customer_repository
        self.customer_validator = customer_validator

    def set_params(self, id, first_name, last_name, document_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.document_number = document_number
        return self

    def execute(self):
        customer = self.customer_repository.get_customer_by_id(id=self.id)
        if self.first_name:
            customer.first_name = self.first_name
        if self.last_name:
            customer.last_name = self.last_name
        if self.document_number:
            customer.document_number = self.document_number
        self.customer_validator.validate(customer)
        return self.customer_repository.update(customer)


class DeleteCustomerInteractor:

    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        customer = self.customer_repository.get_customer_by_id(id=self.id)
        return self.customer_repository.delete(customer)
