from django.db import models

from banking.customers.models import ORMCustomer


class ORMBankAccount(models.Model):
    number = models.IntegerField(unique=True)
    balance = models.DecimalField(decimal_places=2, max_digits=14, blank=True, null=True)
    is_locked = models.BooleanField(default=False)
    customer = models.ForeignKey(ORMCustomer)

    class Meta:
        db_table = 'bank_account'
        verbose_name = 'Bank account'
        verbose_name_plural = 'Bank accounts'

    def __str__(self):
        return '{}: {}'.format(self.customer, self.number)

