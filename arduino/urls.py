# coding:utf-8
from django.conf.urls import url
from arduino import views
from arduino.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
