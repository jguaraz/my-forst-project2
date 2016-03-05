from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.base),
    url(r'^balance$', views.balance0),
    url(r'^diario/new/$', views.diario_new, name='diario_new'),
]
