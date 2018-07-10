from banking.common.exceptions import EntityDoesNotExistException
from banking.customers.entities import Customer
from banking.customers.models import ORMCustomer


class CustomerRepository:

    def _decode_db_customer(self, customer):
        return Customer(id=customer.id,
                        first_name=customer.first_name,
                        last_name=customer.last_name,
                        document_number=customer.document_number)

    def create(self, customer):
        db_customer = ORMCustomer.objects.create(first_name=customer.first_name,
                                                 last_name=customer.last_name,
                                                 document_number=customer.document_number)
        return self._decode_db_customer(db_customer)

    def get_customer_by_id(self, id):
        try:
            db_customer = ORMCustomer.objects.get(id=id)
            return self._decode_db_customer(db_customer)
        except ORMCustomer.DoesNotExist:
            raise EntityDoesNotExistException()

    def exists_document_number(self, customer_id, document_number):
        if customer_id:
            queryset = ORMCustomer.objects.filter(document_number=document_number).exclude(id=customer_id)
        else:
            queryset = ORMCustomer.objects.filter(document_number=document_number)
        return queryset.exists()

    def get_all_customers(self):
        queryset = ORMCustomer.objects.all()
        customers = []
        for customer in queryset:
            customers.append(self._decode_db_customer(customer))
        return customers

    def update(self, customer):
        db_customer = ORMCustomer.objects.get(id=customer.id)
        db_customer.first_name = customer.first_name
        db_customer.last_name = customer.last_name
        db_customer.document_number = customer.document_number
        db_customer.save()
        return self._decode_db_customer(db_customer)
