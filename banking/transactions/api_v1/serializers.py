from rest_framework import serializers


class TransferSerialize(serializers.Serializer):
    fromAccountNumber = serializers.CharField(max_length=20)
    toAccountNumber = serializers.CharField(max_length=20)
    amount = serializers.DecimalField(max_digits=14, decimal_places=2)
