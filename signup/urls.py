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
	path('upd/', views.updCar, name = 'updateCar'),
	path('updDetails/', views.updDetails, name = 'updateDetails'),

	path('addFlat/', views.addFlat, name = 'addFlat'),
	path('addDetailsFlat', views.addDetailsFlat, name = 'addDetailsFlat'),
	path('updFlat', views.updFlat, name = 'updFlat'),

	path('main/', views.main, name = 'mainpage'),
	path('ua/main/', views.mainUa, name = 'mainpageUa'),

]