from django.contrib import admin


from django.contrib import admin

from banking.accounts.models import ORMBankAccount


@admin.register(ORMBankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('customer', 'number', 'balance', 'type', 'is_locked')
