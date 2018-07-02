from banking.accounts.entitites import BankAccount


class CreateBankAccountInteractor:

    def __init__(self, bank_account_repository):
        self.bank_account_repository = bank_account_repository

    def set_params(self, number, balance, is_locked, customer_id):
        self.number = number
        self.balance = balance
        self.is_locked = is_locked
        self.customer_id = customer_id
        return self

    def execute(self):
        bank_account = BankAccount(number=self.number, balance=self.balance, is_locked=self.is_locked,
                                   customer_id=self.customer_id)
        return self.bank_account_repository.create(bank_account)
