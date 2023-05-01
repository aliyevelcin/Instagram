from django.urls import path
from accounts.views import profile_account

app_name = 'accounts'


urlpatterns = [
    path('profile/<slug:slug>',profile_account,name ='profile_account'),
    # path('profile/<slug:slug>', profileDetailView.as_view(), name='profile'),
]