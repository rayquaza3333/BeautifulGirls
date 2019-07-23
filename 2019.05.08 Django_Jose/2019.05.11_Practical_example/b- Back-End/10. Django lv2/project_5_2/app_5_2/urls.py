from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from app_5_2 import views

urlpatterns = [
    url(r'^access',views.access, name = 'access'),
]
