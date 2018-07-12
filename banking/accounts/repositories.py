from django.core.paginator import Paginator

from banking.accounts.entitites import BankAccount
from banking.accounts.models import ORMBankAccount
from banking.common.exceptions import EntityDoesNotExistException


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
        try:
            db_account = ORMBankAccount.objects.get(number=account_number)
            return self._decode_db_account(db_account)
        except ORMBankAccount.DoesNotExist:
            raise EntityDoesNotExistException('Bank account does not exist')

    def get_all_bank_accounts(self, page_size, page):
        queryset = ORMBankAccount.objects.filter().order_by('number')
        paginator = Paginator(queryset, page_size)
        try:
            queryset = paginator.page(page)
        except Exception:
            queryset = paginator.page(paginator.num_pages)
        bank_accounts = []
        for bank_account in queryset:
            bank_accounts.append(self._decode_db_account(bank_account))
        pagination_data = {
            'count': paginator.count,
            'page_range': list(paginator.page_range),
            'num_pages': paginator.num_pages,
            'per_page': paginator.per_page,
            'page': page
        }
        return bank_accounts, pagination_data

    def update(self, account):
        db_account = ORMBankAccount.objects.get(id=account.id)
        db_account.balance = account.balance
        db_account.is_locked = account.is_locked
        db_account.save()
