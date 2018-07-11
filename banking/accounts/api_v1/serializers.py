

class BankAccountSerialize:

    @staticmethod
    def serialize(account):
        return {
            'id': account.id,
            'number': account.number,
            'balance': account.balance,
            'customerId': account.customer_id,
            'isLocked': account.is_locked
        }
