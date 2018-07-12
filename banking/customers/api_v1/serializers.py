from banking.accounts.api_v1.serializers import BankAccountSerialize


class CustomerSerializer:

    @staticmethod
    def serialize(customer):
        data = {
            'id': customer.id,
            'firstName': customer.first_name,
            'lastName': customer.last_name,
            'documentNumber': customer.document_number
        }
        if customer.bank_accounts:
            bank_accounts = []
            for bank_account in customer.bank_accounts:
                bank_accounts.append(BankAccountSerialize.serialize(bank_account))
            data['bankAccounts'] = bank_accounts
        return data


class CustomersSerializer:

    @staticmethod
    def serialize(customers):
        return [CustomerSerializer.serialize(customer) for customer in customers]
