from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': 'Это главная страница проекта Yatube',
        'posts': posts,
    }
    return render(request, template, context)

def group_list(request):
    template = 'posts/group_list.html'
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)