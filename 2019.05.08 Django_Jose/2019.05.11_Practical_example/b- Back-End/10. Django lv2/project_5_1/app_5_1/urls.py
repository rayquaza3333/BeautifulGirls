from django.conf.urls import url
from app_5_1 import views

urlpatterns = [
    url(r'^access',views.access, name = 'access'),
]
