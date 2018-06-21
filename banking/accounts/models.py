from django.db import models

from banking.customers.models import Customer


class BankAccount(models.Model):
    number = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2)
    is_locked = models.BooleanField()
    customer = models.ForeignKey(Customer)

    def lock(self):
        if not self.is_locked:
            self.is_locked = True

    def unlock(self):
        if self.is_locked:
            self.is_locked = False

    def has_identity(self):
        return True if self.number.strip() else False

    def withdraw_money(self, amount):
        pass
