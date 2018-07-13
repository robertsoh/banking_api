from django.db import models

from banking.common.constants import BANK_ACCOUNT_TYPE_CHOICES, BANK_ACCOUNT_TYPE_SAVINGS_ACCOUNT
from banking.customers.models import ORMCustomer


class ORMBankAccount(models.Model):
    number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(decimal_places=2, max_digits=14, blank=True, null=True)
    is_locked = models.BooleanField(default=False)
    customer = models.ForeignKey(ORMCustomer, related_name='bank_accounts')
    type = models.CharField(max_length=15, choices=BANK_ACCOUNT_TYPE_CHOICES, null=True,
                            default=BANK_ACCOUNT_TYPE_SAVINGS_ACCOUNT)

    class Meta:
        db_table = 'bank_account'
        verbose_name = 'Bank account'
        verbose_name_plural = 'Bank accounts'

    def __str__(self):
        return '{}: {}'.format(self.customer, self.number)
