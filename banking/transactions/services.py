from django.db import transaction

from banking.common.exceptions import Notification, Error


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
            raise Error('amount is missing')
        if amount <= 0:
            notification.add_error('The amount must be greater than zero')

    def validate_bank_accounts(self, notification, origen_account, destination_account):
        if not origen_account or not destination_account:
            raise Error('Cannot perform the transfer. Invalid data in bank accounts specifications')

        if origen_account.number == destination_account.number:
            notification.add_error('Cannot transfer money to the same bank account')
