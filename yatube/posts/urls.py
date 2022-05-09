# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main_page'),
    path('index.html', views.index, name='main_page'),
    path('group_list.html', views.group_list, name='project_groups'),
]
