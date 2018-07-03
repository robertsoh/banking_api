from banking.common.models import EntityDoesNotExistException
from banking.customers.entities import Customer
from banking.customers.models import ORMCustomer


class CustomerRepository:

    def _decode_db_customer(self, customer):
        return Customer(id=customer.id,
                        first_name=customer.first_name,
                        last_name=customer.last_name)

    def create(self, customer):
        db_customer = ORMCustomer.objects.create(first_name=customer.first_name,
                                                 last_name=customer.last_name)
        return self._decode_db_customer(db_customer)

    def get_customer_by_id(self, id):
        try:
            db_customer = ORMCustomer.objects.get(id=id)
            return self._decode_db_customer(db_customer)
        except ORMCustomer.DoesNotExist:
            raise EntityDoesNotExistException()
