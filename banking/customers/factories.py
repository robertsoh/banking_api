from banking.customers.api_v1.views import CustomerView
from banking.customers.repositories import CustomerRepository
from banking.customers.interactors import CreateCustomerInteractor, GetAllCustomersInteractor, UpdateCustomerInteractor
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


def create_customers_view(request, **kwargs):
    return CustomerView(create_customer_interactor=create_create_customer_interactor(),
                        get_all_customers_interactor=create_get_all_customers_interactor(),
                        update_customer_interactor=create_update_customer_interactor())
