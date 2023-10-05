from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog' #namespace

urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo')
]