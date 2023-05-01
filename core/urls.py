from django.urls import path
from core.views import mainpage , explore , login


app_name = 'core'


urlpatterns = [
    path('',mainpage,name ='main'),
    path('exp/',explore,name ='explore'),
    path('login/',login,name ='login'),

    

]