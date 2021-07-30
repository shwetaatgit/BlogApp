from django.shortcuts import render
from django.views import generic
from .models import blog

class BlogList(generic.ListView):
    queryset = blog.objects.order_by('-published_on')
    template_name = 'home.html'

class BlogDetail(generic.DetailView):
    model = blog
    template_name = 'blog_detail.html'