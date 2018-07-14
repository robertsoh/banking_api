from banking.accounts.api_v1.serializers import BankAccountSerialize, BankAccountsSerialize
from banking.common.decorators import serialize_exceptions
from banking.common.paginators import CustomPagination


class BankAccountListCreateView:

    def __init__(self,
                 create_bank_account_interactor=None,
                 get_all_bank_accounts_interactor=None):
        self.create_bank_account_interactor = create_bank_account_interactor
        self.get_all_bank_accounts_interactor = get_all_bank_accounts_interactor

    @serialize_exceptions
    def post(self, data):
        """
        ::param number: 'Número de cuenta bancaria'
        ::param balance: 'Saldo de la cuenta'
        ::param isLocked: 'Bloquear la cuenta'
        ::param type: 'Tipo de cuenta bancaria: SAVINGS_ACCOUNT, CURRENT_ACCOUNT, SALARY_ACCOUNT'
        :return:
            ::param id: 'Id de la cuenta bancaria'
            ::param number: 'Número de cuenta bancaria'
            ::param balance: 'Saldo de la cuenta'
            ::param isLocked: 'Bloquear la cuenta'
            ::param type: 'Tipo de cuenta bancaria: SAVINGS_ACCOUNT, CURRENT_ACCOUNT, SALARY_ACCOUNT'
        """
        customer = self.create_bank_account_interactor.set_params(
            number=data.get('number'),
            balance=data.get('balance'),
            is_locked=data.get('isLocked'),
            customer_id=data.get('customerId'),
            type=data.get('type')
            ).execute()
        body = BankAccountSerialize.serialize(customer)
        status = 201
        return body, status

    @serialize_exceptions
    def get(self, page_size=None, page=None):
        """
        :param page_size: El tamaño de la paginación
        :param page: Número de página que desea consultar
        :return: asdasd
        """
        custom_pagination = CustomPagination(page_size=page_size, page=page)
        cleaned_data = custom_pagination.cleaned_data()
        bank_accounts, pagination_data = self.get_all_bank_accounts_interactor.set_params(
            page_size=cleaned_data.get('page_size'),
            page=cleaned_data.get('page')
            ).execute()
        body = custom_pagination.set_params(queryset=BankAccountsSerialize.serialize(bank_accounts),
                                            count=pagination_data.get('count'),
                                            page_range=pagination_data.get('page_range')
                                            ).paginate_queryset()
        status = 200
        return body, status


class BankAccountRetrieveUpdateView:

    def __init__(self,
                 get_bank_account_interactor=None,
                 update_bank_account_interactor=None):
        self.get_bank_account_interactor = get_bank_account_interactor
        self.update_bank_account_interactor = update_bank_account_interactor

    @serialize_exceptions
    def get(self, account_id):
        bank_account = self.get_bank_account_interactor.set_params(id=account_id).execute()
        body = BankAccountSerialize.serialize(bank_account)
        status = 200
        return body, status

    @serialize_exceptions
    def patch(self, data):
        bank_account = self.update_bank_account_interactor.set_params(
            id=data.get('account_id'),
            balance=data.get('balance'),
            is_locked=data.get('isLocked')
            ).execute()
        body = BankAccountSerialize.serialize(bank_account)
        status = 200
        return body, status
