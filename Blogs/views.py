from django.shortcuts import redirect, render
from .models import blog
from . import forms

def BlogList(request):
    blogs = blog.objects.all()
    context ={
        'blog_list': blogs
    }
    return render(request, "home.html", context)

def BlogDetail(request, slug):
    blogs_detail = blog.objects.get(slug=slug)
    context ={
        'blogs': blogs_detail
    }
    return render(request, "blog_detail.html", context)

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