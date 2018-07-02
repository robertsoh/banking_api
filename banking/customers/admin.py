from django.contrib import admin

from banking.customers.models import ORMCustomer


@admin.register(ORMCustomer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
