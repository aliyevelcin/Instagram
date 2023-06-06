from django.urls import path
from core.views import MainView , ExploreView ,StoryView
# login


app_name = 'core'


urlpatterns = [
    path('',MainView.as_view(),name ='main'),
    path('exp/',ExploreView.as_view() ,name ='explore'),
    path('story/',StoryView.as_view() ,name ='story'),
    

]