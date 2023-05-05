from django.urls import path
from accounts.views import profile_account ,register,login  


app_name = 'accounts'


urlpatterns = [
    path('profile/<slug:slug>',profile_account,name ='profile_account'),
    path('register/',register,name ='register'),
    path('login/',login,name ='login'),

    
 


]