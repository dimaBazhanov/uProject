from django.contrib.auth import login as auth_login, authenticate, logout, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileForm, userPreferencesForm, car, carDetails
from .models import car as Car, carDetails as details
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile

# TODO Update form for car of particular organization
def updDetails(request):
    details_form = carDetails()
    if request.user.is_authenticated:
        current_user = User.objects.get(username = request.user.username)
        user_cars = Car.objects.filter(user = current_user)

        if request.method == 'POST':
            details_form = carDetails(request.POST)
            if details_form.is_valid():
                current_car_id = request.POST.getlist('cars', None)
                current_car = Car.objects.get(id = current_car_id[0])

                current_details = details.objects.get(car = current_car)

                if request.POST.get('radio') == 'on':
                    current_details.radio = True
                else:
                    current_details.radio = False
                if request.POST.get('display') == 'on':
                    current_details.display = True
                else:
                    current_details.display = False
                if request.POST.get('airConditioner') == 'on':
                    current_details.airConditioner = True
                else:
                    current_details.airConditioner = False
                if request.POST.get('glassFogging') == 'on':
                    current_details.glassFogging = True
                else:
                    current_details.glassFogging = False
                if request.POST.get('lights') == 'on':
                    current_details.lights = True
                else:
                    current_details.lights = False
                    
                current_details.inside = request.POST.get('inside')
                current_details.price = request.POST.get('price')
                current_details.colour = request.POST.get('colour')

                current_details.save()

                return redirect('login')
    context = {'detailsForm':details_form, 'cars':user_cars}
    return render(request, 'signup/updDetails.html', context)

def updCar(request):
    car_form = car()
    if request.user.is_authenticated:
        current_user = User.objects.get(username = request.user.username)
        user_cars = Car.objects.filter(user = current_user)

        if request.method == 'POST':
            car_form = car(request.POST)
            if car_form.is_valid():
                #edit = car_form.save(commit=False)
                current_car_id = request.POST.getlist('cars', None)
                print(current_car_id)

                current_car = Car.objects.get(id = current_car_id[0])

                current_car.mark = request.POST.get('mark')
                current_car.model = request.POST.get('model')
                current_car.city = request.POST.get('city')
                current_car.county = request.POST.get('county')
                current_car.location = request.POST.get('location')

                current_car.save()

                return redirect('login')
    context = {'carForm':car_form, 'cars':user_cars}
    return render(request, 'signup/updCar.html', context)

def addCar(request):
    car_form = car()
    carDetails_form = carDetails()
    if request.user.is_authenticated:
        if request.method == 'POST':
            car_form = car(request.POST)
            #carDetails_form = carDetails(request.POST)
            if car_form.is_valid():
                newcar = car_form.save(commit=False)
                newcar.mark = request.POST.get('mark')
                newcar.model = request.POST.get('model')
                newcar.city = request.POST.get('city')
                newcar.county = request.POST.get('county')
                newcar.location = request.POST.get('location')
                newcar.user = request.user # раньше было так
                '''
                newcar.user = request.user.username с ошибкой, в newcar.user нужно передать объект user казалось бы
                что может быть проще чем исправить это? Ну вообщем через пол часа дошло, как по мне отличная аналогия
                к моему скиллу программирования это ребенок пытающийся засунуть в отверстее для круга треугольник =/
                '''
                newcar.save()
                details = carDetails_form.save(commit=False)
                details.car = newcar
                details.save()

                #if carDetails_form.is_valid():
                    #carDetails_form.save(commit=False)
                    #carDetails_form.car_id = car_form
                    #carDetails_form.save()
                return redirect('login')
        context = {'carForm':car_form, 'detailsForm':carDetails_form}
        return render(request, 'signup/addCar.html', context)
    else:
        return redirect('login')

def addDetails(request):
    if request.user.is_authenticated:
        carDetails_form = carDetails()

        if request.method == 'POST':
            carDetails_form = carDetails(request.POST)
            if carDetails_form.is_valid():
                carDetails_form.save()
                return redirect('login')

        context = {'detailsForm':carDetails_form}
        return render(request, 'signup/addDetails.html', context)
    else:
        return redirect('login')

def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form' : form}
    return render(request, 'signup/signup.html', context)

@login_required
@transaction.atomic
def pref(request):
    if request.method == 'POST':
        pref_form = userPreferencesForm(request.POST, instance=request.user.userpreferences)
        if  pref_form.is_valid():
            pref_form.save()
            messages.success(request, ('Ваши настройки были успешно обновлены!'))
            return redirect('home')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        pref_form = userPreferencesForm(instance=request.user.userpreferences)
    username = request.user.username
    context = {'username':username, 'pref_form': pref_form}
    return render(request, 'signup/pref.html', context)


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('home')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('preferences')
    return render(request, 'signup/login.html')

def showUser(request):

    return render(request, 'signup/pref.html')



@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect('home')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = SignUpForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    username = request.user.username
    context = {'username':username, 'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'signup/aboutUser.html', context)