from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:f>/', views.friend, name='friend'),
     path('group/<str:g>/', views.group, name='group'),
 #   path('login/', views.login, name = 'login'),
]