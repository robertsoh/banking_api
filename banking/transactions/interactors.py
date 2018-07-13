from django.db import transaction

from banking.transactions.entities import Transaction


class CreateTransferInteractor:

    def __init__(self, bank_account_repository, transfer_validator, transfer_domain_service):
        self.bank_account_repository = bank_account_repository
        self.transfer_validator = transfer_validator
        self.transfer_domain_service = transfer_domain_service

    def set_params(self, origen_account, destination_account, amount):
        self.origen_account = origen_account
        self.destination_account = destination_account
        self.amount = amount
        return self

    def execute(self):
        transaction = Transaction(origen_account=self.origen_account,
                                  destination_account=self.destination_account,
                                  amount=self.amount)
        transaction = self.transfer_validator.validate(transaction)
        self.perform_transfer(transaction)

    @transaction.atomic
    def perform_transfer(self, transaction):
        self.transfer_domain_service.perform_transfer(transaction.origen_account,
                                                      transaction.destination_account,
                                                      transaction.amount)
        self.bank_account_repository.update(transaction.origen_account)
        self.bank_account_repository.update(transaction.destination_account)
