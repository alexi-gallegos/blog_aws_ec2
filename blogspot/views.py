from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogspot/index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blogspot/post_detail.html'
