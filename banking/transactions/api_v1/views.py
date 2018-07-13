from banking.common.decorators import serialize_exceptions


class CreateTransferView:

    def __init__(self, create_transfer_interactor=None):
        self.create_transfer_interactor = create_transfer_interactor

    @serialize_exceptions
    def post(self, data):
        self.create_transfer_interactor.set_params(
            origen_account=data.get('fromAccountNumber'),
            destination_account=data.get('toAccountNumber'),
            amount=data.get('amount')
        ).execute()
        body = 'Transfer done!'
        status = 201
        return body, status
