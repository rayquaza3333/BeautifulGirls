from django.contrib import admin
from django.urls import path
from app_URL import views
from django.conf.urls import url, include

app_name = 'app_URL'

urlpatterns = [
    url(r'^relative/$',views.relative, name = 'relative'),
    url(r'^base/',views.base, name = 'base'),
    url(r'^other/',views.other, name = 'other'),
]
