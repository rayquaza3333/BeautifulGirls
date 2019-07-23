from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app_two import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
]
