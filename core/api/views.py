from core.models import Post
from rest_framework.generics import ListAPIView
from .serializer import PostSerializer

class PostsAPIView(ListAPIView):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()