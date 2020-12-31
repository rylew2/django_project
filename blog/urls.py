from django.urls import path

from . import views

# trailing slashes like about/ are best practice if url includes trailing slash
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
