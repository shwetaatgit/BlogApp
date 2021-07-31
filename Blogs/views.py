from django.shortcuts import redirect, render
from django.views import generic
from .models import blog
from . import forms

class BlogList(generic.ListView):
    queryset = blog.objects.order_by('-published_on')
    template_name = 'home.html'

class BlogDetail(generic.DetailView):
    model = blog
    template_name = 'blog_detail.html'

def createblog(request):
    if request.method=='POST':
        form= forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form= forms.CreateBlog()
    return render(request, 'create_blog.html',{'form':form})