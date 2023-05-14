from django.shortcuts import render
from core.models import Post
from accounts.models import User

def mainpage(request):
    users = User.objects.all()
    posts = Post.objects.order_by('-id')
    context = {
        'posts':posts,
        'users': users
    }
    return render(request, 'insta.html', context)

def explore(request):
    posts = Post.objects.order_by('-id')
    users = User.objects.all()

    context = {
        'posts':posts,
        'users':users
    }
    return render(request, 'explore.html', context)



# Create your views here.
