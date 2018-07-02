from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from banking.accounts.api_v1.serializers import BankAccountSerialize


class BankAccountView(CreateAPIView):
    serializer_class = BankAccountSerialize

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.perform_create(serializer)
        return Response(data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()
