from banking.customers.api_v1.views import CustomerView
from banking.customers.repositories import CustomerRepository
from banking.customers.interactors import CreateCustomerInteractor


def customer_repository_factory():
    return CustomerRepository()


def create_customer_interactor():
    return CreateCustomerInteractor(customer_repository=customer_repository_factory())


def create_customers_view(requests, **kwargs):
    return CustomerView(create_customer_interactor=create_customer_interactor())
