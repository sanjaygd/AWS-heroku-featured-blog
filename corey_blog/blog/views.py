from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'

