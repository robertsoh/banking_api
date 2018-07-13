

class BankAccountSerialize:

    @staticmethod
    def serialize(account):
        data = {
            'id': account.id,
            'number': account.number,
            'type': account.get_type_display()
        }
        if account.balance:
            data['balance'] = account.balance
        if account.customer_id:
            data['customerId'] = account.customer_id
        if account.is_locked:
            data['isLocked'] = account.is_locked
        return data


class BankAccountsSerialize:

    @staticmethod
    def serialize(bank_accounts):
        return [BankAccountSerialize.serialize(bank_account) for bank_account in bank_accounts]
