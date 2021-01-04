from django.urls import path

from . import views
from .views import (PostCreateView, PostDeleteView, PostDetailView,
                    PostListView, PostUpdateView, UserPostListView)

# trailing slashes like about/ are best practice if url includes trailing slash
urlpatterns = [

    # naming_conventions
    # https://stackoverflow.com/questions/50755550/what-are-naming-rules-of-templates-in-django-class-based-views
    # Example: if model name is Abcd
    # for ListView: abcd_list.html
    # for CreateView: abcd_form.html
    # for DetailView: abcd_detail.html
    # for DeleteView: abcd_confirm_delete.html
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
]
