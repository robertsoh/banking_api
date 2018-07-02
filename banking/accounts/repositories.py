from banking.accounts.entitites import BankAccount
from banking.accounts.models import ORMBankAccount


class BankAccountRepository:

    def create(self, account):
        db_account = ORMBankAccount.objects.create(number=account.number, balance=account.balance,
                                                   is_locked=account.is_locked, customer_id=account.customer_id)
        return self._decode_db_account(db_account)

    def _decode_db_account(self, account):
        return BankAccount(id=account.id,
                           number=account.number,
                           balance=account.balance,
                           is_locked=account.is_locked,
                           customer_id=account.customer_id)
