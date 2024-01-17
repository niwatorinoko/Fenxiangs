from django.shortcuts import render
from django.views import generic
from post.models import Post

# Create your views here.
class PostListView(generic.ListView):
    template_name = "post/list.html"
    model = Post