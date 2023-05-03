from django.shortcuts import render, redirect
from accounts.models import User

def profile_account(request, slug):
    user = User.objects.get(slug=slug)
    context = {
        'user':user
    }
    return render(request, 'profile.html', context)
 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        user = User.objects.create(username=username, first_name=firstname, last_name=lastname, password=password)
        
        return redirect('/')
    return render(request, 'register.html')
# Create your views here.
