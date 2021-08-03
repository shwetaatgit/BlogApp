from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList, name='home'),
    path('create/', views.createblog, name="create_blog"),
    path('<slug:slug>/', views.BlogDetail, name='blog_detail'),
]