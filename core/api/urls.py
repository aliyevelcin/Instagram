from django.urls import path
from .views import PostsAPIView

app_name = 'api'


urlpatterns = [
    path('posts/', PostsAPIView.as_view(), name='posts')
]