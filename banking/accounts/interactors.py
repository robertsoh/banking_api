from banking.accounts.entitites import BankAccount


class CreateBankAccountInteractor:

    def __init__(self, bank_account_repository, bank_account_validator):
        self.bank_account_repository = bank_account_repository
        self.bank_account_validator = bank_account_validator

    def set_params(self, number, balance, is_locked, customer_id, type):
        self.number = number
        self.balance = balance
        self.is_locked = is_locked
        self.customer_id = customer_id
        self.type = type
        return self

    def execute(self):
        bank_account = BankAccount(number=self.number, balance=self.balance, is_locked=self.is_locked,
                                   customer_id=self.customer_id, type=self.type)
        bank_account = self.bank_account_validator.validate(bank_account)
        return self.bank_account_repository.create(bank_account)


class GetAllBankAccountsInteractor:

    def __init__(self, bank_account_repository):
        self.bank_account_repository = bank_account_repository

    def set_params(self, page_size, page):
        self.page_size = page_size
        self.page = page
        return self

    def execute(self):
        return self.bank_account_repository.get_all_bank_accounts(page_size=self.page_size, page=self.page)


class GetBankAccountInteractor:

    def __init__(self, bank_account_repository):
        self.bank_account_repository = bank_account_repository

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.bank_account_repository.get_bank_account_by_id(self.id)


class UpdateBankAccountInteractor:

    def __init__(self, bank_account_repository, bank_account_validator):
        self.bank_account_repository = bank_account_repository
        self.bank_account_validator = bank_account_validator

    def set_params(self, id, balance, is_locked):
        self.id = id
        self.balance = balance
        self.is_locked = is_locked
        return self

    def execute(self):
        bank_account = self.bank_account_repository.get_bank_account_by_id(id=self.id)
        if self.balance:
            bank_account.balance = self.balance
        if self.is_locked is not None:
            bank_account.is_locked = self.is_locked
        bank_account = self.bank_account_validator.validate(bank_account)
        return self.bank_account_repository.update(bank_account)
