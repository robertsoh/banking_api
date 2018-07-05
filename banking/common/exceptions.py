

class Error(Exception):

    def __init__(self, message=None, cause=None):
        self.message = message
        self.cause = cause

    def get_message(self):
        return self.message


class Notification:

    def __init__(self):
        self.errors = []

    def add_error(self, message, exception=None):
        self.errors.append(Error(message, exception))

    def has_errors(self):
        return True if self.errors else False

    def error_message(self):
        return ", ".join([error.get_message() for error in self.errors])


class EntityDoesNotExistException(Error):

    def __init__(self, message='Entity not found'):
        super().__init__(message)
