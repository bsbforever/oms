from django.conf.urls import  url, include
from oracle import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
]
