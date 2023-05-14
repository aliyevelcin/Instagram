from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.hashers import make_password

def profile_account(request, slug):
    user = User.objects.get(slug=slug)
    context = {
        'user':user
    }
    return render(request, 'profile.html', context)
 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        user = User.objects.create(username=username, first_name=firstname, last_name=lastname, password=make_password(password))
        
        return redirect('/accounts/login/')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        dj_login(request,user)
        return redirect('/')
    return render(request, 'login.html')
 



def update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
         
        user = authenticate(request, username=username )
        dj_update(request,user)
        return redirect('/')
    return render(request, 'update.html')
 
# Create your views here.
