from django.conf.urls import url

from banking.common.views import ViewWrapper
from banking.customers.factories import create_customers_view


urlpatterns = [
    url(
        r'^customers$',
        ViewWrapper.as_view(view_creator_func=create_customers_view),
        name='customers'
    ),
]
