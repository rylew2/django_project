from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Post

# class based view options ==> listviews, detailsviews, updateviews, createviews
# blogs will be listview , if you click on blog it should go to "detailsview"
# when you go to update blog it will be update view

# Create your views here.

# function based views (but good candidate for listview)


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context=context)


class PostListView(ListView):
    model = Post

    # <app> / <model>_<class view type>.html
    # by default it's looking for ==> blog/post_list.html  - so we change it
    template_name = 'blog/home.html'

    # by default, listview calls context model object ==> ObjectList
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post

    # <app> / <model>_<class view type>.html
    # by default it's looking for ==> blog/post_list.html  - so we change it
    template_name = 'blog/user_posts.html'

    # by default, listview calls context model object ==> ObjectList
    context_object_name = 'posts'
    paginate_by = 5

    # modify default queryset
    def get_queryset(self):
        # get object from db if it exists, otherwise 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # <app> / <model>_<class view type>.html
    # looking for template ==>  blog/post_detail


# to restrict this route to only admins - for class based views we can use a LoginRequiredMixin
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # after Post creation, redirect to
    def get_success_url(self) -> str:
        return reverse('post-detail', kwargs={'pk': self.object.pk})


# to restrict this route to only admins - for class based views we can use a LoginRequiredMixin
# to allow a test for only author to be able to update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # <app> / <model>_<class view type>.html
    # looking for template ==>  blog/post_detail
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')
