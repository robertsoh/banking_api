from banking.customers.api_v1.views import CustomerView
from banking.customers.repositories import CustomerRepository
from banking.customers.interactors import CreateCustomerInteractor


def create_customer_repository():
    return CustomerRepository()


def create_customer_interactor():
    return CreateCustomerInteractor(customer_repository=create_customer_repository())


def create_customers_view(requests, **kwargs):
    return CustomerView(create_customer_interactor=create_customer_interactor())
