

class ErrorValidationSerializer:

    @staticmethod
    def serialize(exception):
        return {
                   'errors': [
                       exception.get_message()
                   ]
               }
