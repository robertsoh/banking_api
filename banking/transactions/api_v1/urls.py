from django.conf.urls import url

from banking.common.views import ViewWrapper
from banking.transactions.factories import create_create_transfer_view

urlpatterns = [
    url(r'^transfers$',
        ViewWrapper.as_view(view_creator_func=create_create_transfer_view),
        name='transfers'),
]
