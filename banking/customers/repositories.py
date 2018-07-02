from banking.customers.entities import Customer
from banking.customers.models import ORMCustomer


class CustomerRepository:

    def create(self, customer):
        customer = ORMCustomer.objects.create(first_name=customer.first_name,
                                              last_name=customer.last_name)
        return self._decode_db_customer(customer)

    def _decode_db_customer(self, customer):
        return Customer(id=customer.id,
                        first_name=customer.first_name,
                        last_name=customer.last_name)
