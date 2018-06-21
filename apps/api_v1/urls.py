from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^test/$', views.TestView.as_view(), name='test'),
]
