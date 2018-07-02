

class CustomerSerializer:

    @staticmethod
    def serialize(customer):
        return {
            'id': customer.id,
            'firstName': customer.first_name,
            'lastName': customer.last_name
        }
