from django.conf.urls import url

from banking.customers.api_v1.views import CustomerView

urlpatterns = [
    url(r'^customers$', CustomerView.as_view(), name='customers'),
]
