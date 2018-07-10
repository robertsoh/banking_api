from banking.customers.api_v1.views import CustomerListCreateView, CustomerRetrieveUpdateDeleteView
from banking.customers.repositories import CustomerRepository
from banking.customers.interactors import (CreateCustomerInteractor, GetAllCustomersInteractor,
                                           UpdateCustomerInteractor, DeleteCustomerInteractor, GetCustomerInteractor)
from banking.customers.validators import CustomerValidator


def create_customer_repository():
    return CustomerRepository()


def create_customer_validator():
    return CustomerValidator(customer_repository=create_customer_repository())


def create_create_customer_interactor():
    return CreateCustomerInteractor(customer_repository=create_customer_repository(),
                                    customer_validator=create_customer_validator())


def create_update_customer_interactor():
    return UpdateCustomerInteractor(customer_repository=create_customer_repository(),
                                    customer_validator=create_customer_validator())


def create_get_all_customers_interactor():
    return GetAllCustomersInteractor(customer_repository=create_customer_repository())


def create_get_customer_interactor():
    return GetCustomerInteractor(customer_repository=create_customer_repository())


def create_delete_customer_interactor():
    return DeleteCustomerInteractor(customer_repository=create_customer_repository())


def create_customer_list_create_view(request, **kwargs):
    return CustomerListCreateView(
        create_customer_interactor=create_create_customer_interactor(),
        get_all_customers_interactor=create_get_all_customers_interactor()
    )


def create_customer_retrieve_update_delete_view(request, **kwargs):
    return CustomerRetrieveUpdateDeleteView(
        get_customer_interactor=create_get_customer_interactor(),
        update_customer_interactor=create_update_customer_interactor(),
        delete_customer_interactor=create_delete_customer_interactor()
    )
