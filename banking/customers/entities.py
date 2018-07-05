

class Customer(object):
    """
    here is the business logic of Customer entity
    """

    def __init__(self, first_name, last_name, document_number, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.document_number = document_number
        self.id = id
