from banking.common.constants import DEFAULT_PAGINATOR_PAGE_SIZE, DEFAULT_PAGINATOR_PAGE


class ErrorValidationSerializer:

    @staticmethod
    def serialize(exception):
        return {
                   'errors': [
                       exception.get_message()
                   ]
               }
