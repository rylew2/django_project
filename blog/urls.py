from django.urls import path
from . import views

urlpatterns = [
    path('', views, name='blog-home'),
]
