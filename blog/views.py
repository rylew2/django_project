from django.http import HttpResponse
from django.shortcuts import render

posts = [

    {
        'author': 'RyanMS',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'June 15, 2020'
    }
]

# Create your views here.


def home(request):
    context = {
        'posts': posts,
        'title': 'mytitle'
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
