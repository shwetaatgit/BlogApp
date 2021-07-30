from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
]

