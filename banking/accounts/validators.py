import re

from banking.common.constants import BANK_ACCOUNT_TYPE_CHOICES
from banking.common.exceptions import Notification, Error


class BankAccountValidator:

    def __init__(self, bank_account_repository, customer_repository):
        self.bank_account_repository = bank_account_repository
        self.customer_repository = customer_repository

    def validate(self, bank_account):
        notification = Notification()
        self.validate_customer_id(notification, bank_account)
        self.validate_number(notification, bank_account)
        self.validate_balance(notification, bank_account)
        self.validate_is_locked(notification, bank_account)
        self.validate_type(notification, bank_account)
        if notification.has_errors():
            raise Error(notification.error_message())
        return bank_account

    def validate_customer_id(self, notification, bank_account):
        value = bank_account.customer_id
        if not value:
            raise Error('Customer id is required')
        try:
            value = int(value)
        except (ValueError, TypeError):
            raise Error('Customer id must be a integer number')
        self.customer_repository.get_customer_by_id(value)
        bank_account.customer_id = value

    def validate_number(self, notification, bank_account):
        value = bank_account.number
        if not value:
            raise Error('Account number is required')
        try:
            value = str(value)
        except (ValueError, TypeError):
            raise Error('Account number is not valid')
        if not re.match('([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4})$', value):
            raise Error('Account number is not valid')
        if self.bank_account_repository.exists_account_number(bank_account.id, value):
            raise Error('Account number already exists')
        bank_account.number = value

    def validate_balance(self, notification, bank_account):
        value = bank_account.balance
        if not value:
            raise Error('Balance is required')
        try:
            value = float(value)
        except (ValueError, TypeError):
            notification.add_error('Balance number must be a decimal number')
        bank_account.balance = value

    def validate_is_locked(self, notification, bank_account):
        value = bank_account.is_locked
        if value and type(value) != bool:
            notification.add_error('Is locked must be a boolean value')
        bank_account.is_locked = value or False

    def validate_type(self, notification, bank_account):
        value = bank_account.type
        if value not in [type[0] for type in BANK_ACCOUNT_TYPE_CHOICES]:
            notification.add_error('Type is not a valid choice')
