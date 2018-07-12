from django.core.paginator import Paginator

from banking.accounts.entitites import BankAccount
from banking.common.exceptions import EntityDoesNotExistException
from banking.common.paginators import CustomPagination
from banking.customers.entities import Customer
from banking.customers.models import ORMCustomer


class CustomerRepository:

    def _decode_db_customer(self, customer):
        return Customer(id=customer.id,
                        first_name=customer.first_name,
                        last_name=customer.last_name,
                        document_number=customer.document_number)

    def _decode_bank_accounts(self, db_bank_accounts):
        bank_accounts = []
        for db_bank_account in db_bank_accounts.filter(is_locked=False):
            bank_accounts.append(BankAccount(id=db_bank_account.id,
                                             number=db_bank_account.number))
        return bank_accounts

    def _decode_db_customer_bank_accounts(self, customer):
        return Customer(id=customer.id,
                        first_name=customer.first_name,
                        last_name=customer.last_name,
                        document_number=customer.document_number,
                        bank_accounts=self._decode_bank_accounts(customer.bank_accounts))

    def create(self, customer):
        db_customer = ORMCustomer.objects.create(first_name=customer.first_name,
                                                 last_name=customer.last_name,
                                                 document_number=customer.document_number)
        return self._decode_db_customer(db_customer)

    def get_customer_by_id(self, id):
        try:
            db_customer = ORMCustomer.objects.get(id=id)
            return self._decode_db_customer_bank_accounts(db_customer)
        except ORMCustomer.DoesNotExist:
            raise EntityDoesNotExistException("Customer does not exists")

    def exists_document_number(self, customer_id, document_number):
        if customer_id:
            queryset = ORMCustomer.objects.filter(document_number=document_number).exclude(id=customer_id)
        else:
            queryset = ORMCustomer.objects.filter(document_number=document_number)
        return queryset.exists()

    def get_all_customers(self, page_size, page):
        queryset = ORMCustomer.objects.filter(is_active=True).order_by('last_name')
        paginator = Paginator(queryset, page_size)
        try:
            queryset = paginator.page(page)
        except Exception:
            queryset = paginator.page(paginator.num_pages)
        customers = []
        for customer in queryset:
            customers.append(self._decode_db_customer(customer))
        pagination_data = {
            'count': paginator.count,
            'page_range': list(paginator.page_range),
            'num_pages': paginator.num_pages,
            'per_page': paginator.per_page,
            'page': page
        }
        return customers, pagination_data

    def update(self, customer):
        db_customer = ORMCustomer.objects.get(id=customer.id)
        db_customer.first_name = customer.first_name
        db_customer.last_name = customer.last_name
        db_customer.document_number = customer.document_number
        db_customer.save()
        return self._decode_db_customer(db_customer)

    def delete(self, customer):
        db_customer = ORMCustomer.objects.get(id=customer.id)
        db_customer.is_active = False
        db_customer.save()
        return True
