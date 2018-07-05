from banking.customers.repositories import CustomerRepository
from banking.customers.interactors import CreateCustomerInteractor


def create_customer_repository():
    return CustomerRepository()


def create_customer_interactor():
    return CreateCustomerInteractor(customer_repository=create_customer_repository())
