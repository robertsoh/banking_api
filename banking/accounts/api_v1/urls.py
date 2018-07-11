from django.conf.urls import url
from banking.common.views import ViewWrapper
from banking.accounts.factories import create_bank_account_list_create_view


urlpatterns = [
    url(r'^accounts$',
        ViewWrapper.as_view(view_creator_func=create_bank_account_list_create_view),
        name='accounts'),
]
