from banking.accounts.entitites import BankAccount
from banking.accounts.models import ORMBankAccount


class BankAccountRepository:

    def _decode_db_account(self, account):
        return BankAccount(id=account.id,
                           number=account.number,
                           balance=account.balance,
                           is_locked=account.is_locked,
                           customer_id=account.customer_id)

    def create(self, account):
        db_account = ORMBankAccount.objects.create(number=account.number, balance=account.balance,
                                                   is_locked=account.is_locked, customer_id=account.customer_id)
        return self._decode_db_account(db_account)

    def exists_account_number(self, account_number):
        return ORMBankAccount.objects.filter(number=account_number).exists()

    def find_by_number(self, account_number):
        db_account = ORMBankAccount.objects.get(number=account_number)
        return self._decode_db_account(db_account)

    def update(self, account):
        db_account = ORMBankAccount.objects.get(id=account.id)
        db_account.balance = account.balance
        db_account.is_locked = account.is_locked
        db_account.save()
