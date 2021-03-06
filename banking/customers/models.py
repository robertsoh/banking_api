from django.contrib.auth.models import User
from django.db import models


class ORMCustomer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, null=True)

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

    def full_name(self):
        return '{}, {}'.format(self.last_name, self.first_name)