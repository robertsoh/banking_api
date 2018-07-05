from banking.common.exceptions import Error
from banking.common.serializers import ErrorValidationSerializer


def serialize_exceptions(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Error as e:
            body = ErrorValidationSerializer.serialize(e)
            status = 400
        return body, status
    return func_wrapper