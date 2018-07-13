import re
from decimal import Decimal

from banking.common.exceptions import Notification, Error


class TransferValidator:

    def __init__(self, bank_account_repository):
        self.bank_account_repository = bank_account_repository

    def validate(self, transaction):
        notification = Notification()
        self.validate_amount(notification, transaction)
        self.validate_origen_account(notification, transaction)
        self.validate_destination_account(notification, transaction)
        return transaction

    def validate_amount(self, notification, transaction):
        value = transaction.amount
        if not value:
            raise Error("Amount is required")
        try:
            value = Decimal(value)
        except (ValueError, TypeError):
            notification.add_error('Amount must be a decimal number')
        if value <= 0:
            notification.add_error('Amount must be greater than zero')
        transaction.amount = value

    def validate_origen_account(self, notification, transaction):
        value = transaction.origen_account
        if not value:
            raise Error('Origen account is required')
        try:
            value = str(value)
        except (ValueError, TypeError):
            raise Error('Origen account is not valid')
        if not re.match('([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4})$', value):
            raise Error('Origen account number is not valid')
        try:
            transaction.origen_account = self.bank_account_repository.find_by_number(value)
        except Exception as ex:
            raise Error('Origen account: {}'.format(str(ex)))

    def validate_destination_account(self, notification, transaction):
        value = transaction.destination_account
        if not value:
            raise Error('Destination account is required')
        try:
            value = str(value)
        except (ValueError, TypeError):
            raise Error('Origen account is not valid')
        if not re.match('([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4})$', value):
            raise Error('Destination account number is not valid')
        try:
            transaction.destination_account = self.bank_account_repository.find_by_number(value)
        except Exception as ex:
            raise Error('Destination account: {}'.format(str(ex)))
