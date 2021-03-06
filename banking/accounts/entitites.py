from banking.common.constants import BANK_ACCOUNT_TYPE_CHOICES
from banking.common.exceptions import Notification
from banking.common.utils import choices_to_dict


class BankAccount(object):

    def __init__(self, number, balance=None, is_locked=None, customer_id=None, id=None, type=None):
        self.number = number
        self.balance = balance
        self.is_locked = is_locked
        self.customer_id = customer_id
        self.id = id
        self.type = type

    def lock(self):
        if not self.is_locked:
            self.is_locked = True

    def unlock(self):
        if self.is_locked:
            self.is_locked = False

    def has_identity(self):
        return True if self.number.strip() else False

    def withdraw_money(self, amount):
        notification = self.withdraw_validation(amount)
        if notification.has_errors():
            raise ValueError(notification.error_message())
        self.balance -= amount

    def deposit_money(self, amount):
        notification = self.deposit_validation(amount)
        if notification.has_errors():
            raise ValueError(notification.error_message())
        self.balance += amount

    def withdraw_validation(self, amount):
        notification = Notification()
        self.validate_amount(notification, amount)
        self.validate_bank_account(notification)
        self.validate_balance(notification, amount)
        return notification

    def deposit_validation(self, amount):
        notification = Notification()
        self.validate_amount(notification, amount)
        self.validate_bank_account(notification)
        return notification

    def validate_amount(self, notification, amount):
        if not amount:
            notification.add_error('amount is missing')
            return
        if amount <= 0:
            notification.add_error('The amount must be greater than zero')

    def validate_bank_account(self, notification):
        if not self.has_identity():
            notification.add_error('The account has no identity')
        if self.is_locked:
            notification.add_error('The account is locked')

    def validate_balance(self, notification, amount):
        if self.balance is None:
            notification.add_error('balance cannot be null')
        if not self.can_be_withdrawed(amount):
            notification.add_error('Cannot withdraw in the account, amount is greater than balance')

    def can_be_withdrawed(self, amount):
        return not self.is_locked and self.balance >= amount

    def get_type_display(self):
        return choices_to_dict(BANK_ACCOUNT_TYPE_CHOICES)[self.type]
