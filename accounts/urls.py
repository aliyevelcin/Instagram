from django.urls import path
from accounts.views import profile_account

app_name = 'accounts'


urlpatterns = [
    path('profile/<int:id>',profile_account,name ='profile_account'),
]