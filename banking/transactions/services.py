from django.db import transaction

from banking.common.models import Notification


class TransferDomainService:

    def perform_transfer(self, origen_account, destination_account, amount):
        notification = self.validation(origen_account, destination_account, amount)
        if notification.has_errors():
            raise ValueError(notification.error_message())
        origen_account.withdraw_money(amount)
        destination_account.deposit_money(amount)

    def validation(self, origen_account, destination_account, amount):
        notification = Notification()
        self.validate_amount(notification, amount)
        self.validate_bank_accounts(notification, origen_account, destination_account)
        return notification

    def validate_amount(self, notification, amount):
        if not amount:
            notification.add_error("amount is missing")
            return
        if amount <= 0:
            notification.add_error("The amount must be greater than zero")

    def validate_bank_accounts(self, notification, origen_account, destination_account):
        if not origen_account or not destination_account:
            notification.add_error("Cannot perform the transfer. Invalid data in bank accounts specifications")
            return
        if origen_account.number == destination_account.number:
            notification.add_error("Cannot transfer money to the same bank account")


class TransactionApplicationService:

    def __init__(self, bank_account_repository, transfer_domain_service):
        self.bank_account_repository = bank_account_repository
        self.transfer_domain_service = transfer_domain_service

    @transaction.atomic
    def perform_transfer(self, from_account_number, to_account_number, amount):
        origen_account = self.bank_account_repository.find_by_number(to_account_number)
        destination_account = self.bank_account_repository.find_by_number(from_account_number)
        self.transfer_domain_service.perform_transfer(origen_account, destination_account, amount)
        self.bank_account_repository.update(origen_account)
        self.bank_account_repository.update(destination_account)
