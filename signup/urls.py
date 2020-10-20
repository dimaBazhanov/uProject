from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.signup, name = 'home'),
	path('login/', views.login, name = 'login'),
	path('user/', views.update_profile, name = 'user'),
]