from banking.customers.api_v1.views import CustomerView
from banking.customers.repositories import CustomerRepository
from banking.customers.interactors import CreateCustomerInteractor
from banking.customers.validators import CustomerValidator


def create_customer_repository():
    return CustomerRepository()


def create_customer_validator():
    return CustomerValidator(customer_repository=create_customer_repository())


def create_customer_interactor():
    return CreateCustomerInteractor(customer_repository=create_customer_repository(),
                                    customer_validator=create_customer_validator())


def create_customers_view(request, **kwargs):
    return CustomerView(create_customer_interactor=create_customer_interactor())
