# from banking.accounts.api_v1.views import BankAccountView
from banking.accounts.interactors import CreateBankAccountInteractor
from banking.accounts.repositories import BankAccountRepository


def create_bank_account_repository():
    return BankAccountRepository()


def create_bank_account_interactor():
    return CreateBankAccountInteractor(bank_account_repository=create_bank_account_repository())
