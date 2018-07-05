from banking.common.exceptions import Error, Notification


class CustomerValidator:

    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def validate(self, customer):
        notification = Notification()
        self.validate_document_number(notification, customer.document_number)
        if notification.has_errors():
            raise Error(notification.error_message())

    def validate_document_number(self, notification, value):
        if self.customer_repository.exists_document_number(value):
            notification.add_error("Document number already exists")
            return
