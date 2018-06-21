from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('banking.accounts.api_v1.urls', namespace='api_v1')),
]
