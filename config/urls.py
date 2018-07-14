from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Banking API - ADS')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^api/v1/', include('banking.customers.api_v1.urls', namespace='api_customers')),
    url(r'^api/v1/', include('banking.accounts.api_v1.urls', namespace='api_accounts')),
    url(r'^api/v1/', include('banking.transactions.api_v1.urls', namespace='api_transactions')),
]
