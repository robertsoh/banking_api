from django.conf.urls import url

from banking.transactions.api_v1.views import TransferView

urlpatterns = [
    url(r'^transfers/$', TransferView.as_view(), name='transfers'),
]
