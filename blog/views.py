from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import Post


def get_profile(httpRequest):
    return HttpResponse('Hello world')


def get_my_age(httpRequest):
    return HttpResponse('17')


def get_posts(request):
    methot_post = request.method
    if methot_post == 'POST':
        post = Post.objects.create(title='Good Morning',
                                   description='Have a good day')
        return HttpResponse('Put to the our posts')
    elif methot_post == 'DELETE':
        post = Post.objects.get(id=1)
        post.delete()
        return HttpResponse('Deleted')
    elif methot_post == 'PUT':
        post = Post.objects.get(id=1)
        post.title = 'Good evening'
        post.description = 'Good night'
        post.save()
        return HttpResponse('Changed')
    elif methot_post == 'GET':
        post_all = Post.objects.all()
        return HttpResponse(post_all)


def get_all_posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts_list.html')


class PostView(ListView):
    model = Post
    template_name = 'posts_list.html'

    def get_queryset(self):
        return Post.objects.all()