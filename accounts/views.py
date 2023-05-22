from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.hashers import make_password
from django.views.generic import DetailView, CreateView
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from accounts.forms import ThePasswordChangeForm, ResetPasswordConfirmForm, ResetPasswordForm

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


# def update(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
         
#         user = authenticate(request, username=username )
#         dj_update(request,user)
#         return redirect('/')
#     return render(request, 'update.html')
 
class UpdatePasswordView(PasswordChangeView):
    template_name = 'update.html'
    form_class = ThePasswordChangeForm
    success_url = reverse_lazy('accounts:login')


class ForgetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'forget_password.html'
    success_url = reverse_lazy('accounts:login')
    email_template_name = 'password_reset_email.html'


class ResetPasswordView(PasswordResetConfirmView):
    form_class = ResetPasswordConfirmForm
    template_name= "password_reset_confirm.html" 
    success_url = reverse_lazy('accounts:login')