from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Post, Group, User
from .forms import PostForm
import datetime


RECORDS_PER_PAGE = 10


def index(request):
    posts_list = Post.objects.all()
    page_obj = paginator_builder(posts_list, RECORDS_PER_PAGE, request)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts_list = group.posts.all()
    page_obj = paginator_builder(posts_list, RECORDS_PER_PAGE, request)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    cur_user = get_object_or_404(User, username=username)
    posts_list = cur_user.posts.all()
    page_obj = paginator_builder(posts_list, RECORDS_PER_PAGE, request)

    context = {
        'cur_user': cur_user,
        'posts_count': posts_list.count(),
        'page_obj': page_obj,
        'author_no_show_in_post': 1
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'posts/create_post.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.pub_date = datetime.datetime.now()
    post.text = form.cleaned_data['text']
    post.group = form.cleaned_data['group']
    post.save()
    return redirect(reverse('posts:profile', args=[request.user]))


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if not form.is_valid():
        return render(request, 'posts/create_post.html',
                      {'form': form, 'is_edit': 1, 'post': post})
    post.author = request.user
    post.pub_date = datetime.datetime.now()
    post.text = form.cleaned_data['text']
    post.group = form.cleaned_data['group']
    post.id = post_id
    post.save()
    return redirect(reverse('posts:post_detail', args=[post_id]))


def paginator_builder(records_list, records_limit, request):
    page_number = request.GET.get('page')
    paginator = Paginator(records_list, records_limit)
    return paginator.get_page(page_number)
