from banking.accounts.factories import create_bank_account_repository
from banking.transactions.api_v1.views import CreateTransferView
from banking.transactions.interactors import CreateTransferInteractor
from banking.transactions.services import TransferDomainService
from banking.transactions.validators import TransferValidator


def create_transfer_domain_service():
    return TransferDomainService()


def create_transfer_validator():
    return TransferValidator(
        bank_account_repository=create_bank_account_repository()
    )


def create_create_transfer_interactor():
    return CreateTransferInteractor(
        bank_account_repository=create_bank_account_repository(),
        transfer_validator=create_transfer_validator(),
        transfer_domain_service=create_transfer_domain_service()
    )


def create_create_transfer_view(request, **kwargs):
    return CreateTransferView(
        create_transfer_interactor=create_create_transfer_interactor()
    )