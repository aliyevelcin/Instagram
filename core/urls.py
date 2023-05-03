from django.urls import path
from core.views import mainpage , explore 


app_name = 'core'


urlpatterns = [
    path('',mainpage,name ='main'),
    path('exp/',explore,name ='explore'),
 
    

]