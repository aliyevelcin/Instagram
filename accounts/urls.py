from django.urls import path
from accounts.views import ProfileView ,RegisterView,LoginUserView, UpdatePasswordView
# ,UpdateUSerView,update
from django.contrib.auth.views import LogoutView

app_name = 'accounts'


urlpatterns = [
    path('profile/<slug:slug>',ProfileView.as_view(),name ='profile_account'),
    path('register/',RegisterView.as_view(),name ='register'),
    path('login/',LoginUserView.as_view(),name ='login'),
    # path('update/',update,name ='update'),
    path('log-out', LogoutView.as_view(), name='log-out'),
    path('change-password/', UpdatePasswordView.as_view(), name='change-password'),
]