from django.shortcuts import render
from core.models import Post , Story
from accounts.models import User
from django.views.generic import ListView, TemplateView , CreateView
from core.forms import StoryForm
from django.urls import reverse_lazy



class MainView(TemplateView):
    template_name = "insta.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.order_by('-id')
        context["users"] = User.objects.order_by('-id')
        context["storys"] = Story.objects.order_by('-id')

        return context


class ExploreView(ListView):
    model = Post
    template_name = 'explore.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
 
class StoryView(CreateView):
    model = Story
    template_name = 'story.html'
    form_class = StoryForm
    success_url = reverse_lazy('core:main')
     
    
    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)
    
    
