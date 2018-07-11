from banking.accounts.api_v1.views import BankAccountListCreateView
from banking.accounts.interactors import CreateBankAccountInteractor
from banking.accounts.repositories import BankAccountRepository
from banking.accounts.validators import BankAccountValidator
from banking.customers.factories import create_customer_repository


def create_bank_account_repository():
    return BankAccountRepository()


def create_bank_account_validator():
    return BankAccountValidator(bank_account_repository=create_bank_account_repository(),
                                customer_repository=create_customer_repository())


def create_create_bank_account_interactor():
    return CreateBankAccountInteractor(bank_account_repository=create_bank_account_repository(),
                                       bank_account_validator=create_bank_account_validator())


def create_bank_account_list_create_view(request, **kwargs):
    return BankAccountListCreateView(
        create_bank_account_interactor=create_create_bank_account_interactor()
    )
