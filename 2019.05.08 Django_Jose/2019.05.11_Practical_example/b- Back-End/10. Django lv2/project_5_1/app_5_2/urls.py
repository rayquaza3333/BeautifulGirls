from django.conf.urls import url
from app_5_2 import views

urlpatterns = [
    url(r'^$',views.users, name = 'users'),
]
