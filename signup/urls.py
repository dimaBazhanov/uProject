from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.signup, name = 'home'),
	path('login/', views.login, name = 'login'),
	path('logout', views.logoutUser, name = 'logout'),
	path('user/', views.update_profile, name = 'user'),
	path('pref/', views.pref, name='preferences'),

	path('addCar/', views.addCar, name = 'addCar'),
	path('addDetails', views.addDetails, name = 'addDetails')
]