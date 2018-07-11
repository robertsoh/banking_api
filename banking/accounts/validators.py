from banking.common.exceptions import Notification, EntityDoesNotExistException, Error


class BankAccountValidator:

    def __init__(self, bank_account_repository, customer_repository):
        self.bank_account_repository = bank_account_repository
        self.customer_repository = customer_repository

    def validate(self, bank_account):
        notification = Notification()
        self.validate_customer_id(notification, bank_account.customer_id)
        self.validate_number(notification, bank_account.number)
        if notification.has_errors():
            raise Error(notification.error_message())

    def validate_customer_id(self, notificacion, value):
        self.customer_repository.get_customer_by_id(value)

    def validate_number(self, notificacion, value):
        if self.bank_account_repository.exists_account_number(value):
            raise Error('Account number already exists')
