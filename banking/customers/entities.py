

class Customer(object):

    def __init__(self, first_name, last_name, id=None):
        self._first_name = first_name
        self._last_name = last_name
        self._id = id

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name
