from django.http import HttpResponse


def index(request):
    return HttpResponse('Main page')


def group_posts(request, slug):
    return HttpResponse(f'Посты {slug}')
