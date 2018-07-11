from banking.accounts.api_v1.serializers import BankAccountSerialize
from banking.common.decorators import serialize_exceptions


class BankAccountListCreateView:

    def __init__(self, create_bank_account_interactor=None):
        self.create_bank_account_interactor = create_bank_account_interactor

    @serialize_exceptions
    def post(self, data):
        customer = self.create_bank_account_interactor.set_params(
            number=data.get('number'),
            balance=data.get('balance'),
            is_locked=data.get('isLocked'),
            customer_id=data.get('customerId')).execute()
        body = BankAccountSerialize.serialize(customer)
        status = 201
        return body, status
