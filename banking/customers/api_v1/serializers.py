

class CustomerSerializer:

    @staticmethod
    def serialize(customer):
        return {
            'id': customer.id,
            'firstName': customer.first_name,
            'lastName': customer.last_name,
            'documentNumber': customer.document_number
        }


class CustomersSerializer:

    @staticmethod
    def serialize(customers):
        return [CustomerSerializer.serialize(customer) for customer in customers]
