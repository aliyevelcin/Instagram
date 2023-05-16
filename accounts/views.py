from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.hashers import make_password
from django.views.generic import DetailView, CreateView
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# ,UpdateForm
class ProfileView(DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "user"

class RegisterView(CreateView):
    model = User
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')




 
class LoginUserView(LoginView):
    template_name = "login.html"
    form_class = LoginForm


def update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
         
        user = authenticate(request, username=username )
        dj_update(request,user)
        return redirect('/')
    return render(request, 'update.html')
 
# class UpdateUSerView(CreateView):
#     template_name = "update.html"
#     form_class = UpdateForm
# Create your views here.
