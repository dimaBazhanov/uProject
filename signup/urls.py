from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.main, name = 'mainpage'),
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

	path('signup/', views.signup, name = 'home'), # registration
	path('ua/', views.mainUa, name = 'mainpageUa'),

]
# TODO Ссылку на mainpageUa поменять так, что бы вьюшка определяла на какой ты сейчас странице и подгужала 
# нужный аналог на украинском