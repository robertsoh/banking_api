from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from banking.customers.api_v1.serializers import CustomerSerializer
from banking.customers.factories import create_customer_repository


class CustomerView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    page_size = 2

    def __init__(self, *args, **kwargs):
        self.customer_repository = create_customer_repository()
        super().__init__(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.perform_create(serializer)
        return Response(data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        customers = self.customer_repository.get_all_customers()
        return self.get_serializer().to_dict_customers(customers)
