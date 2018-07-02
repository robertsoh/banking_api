from django.conf.urls import url

from banking.accounts.api_v1.views import BankAccountView

urlpatterns = [
    url(r'^accounts/$', BankAccountView.as_view(), name='accounts'),
]
