from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from banking.accounts.factories import create_bank_account_repository
from banking.transactions.api_v1.serializers import TransferSerialize
from banking.transactions.factories import create_transfer_domain_service
from banking.transactions.services import TransactionApplicationService


class TransferView(CreateAPIView):
    serializer_class = TransferSerialize

    def __init__(self, *args, **kwargs):
        self.transaction_application_service = TransactionApplicationService(
            bank_account_repository=create_bank_account_repository(),
            transfer_domain_service=create_transfer_domain_service())
        super().__init__(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('Transfer done!', status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        data = serializer.validated_data
        self.transaction_application_service.perform_transfer(from_account_number=data.get('fromAccountNumber'),
                                                              to_account_number=data.get('toAccountNumber'),
                                                              amount=data.get('amount'))
