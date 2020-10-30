import datetime

from django.contrib.auth import login as auth_login, authenticate, logout, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileForm, userPreferencesForm, car, carDetails, flat, flatDetails
from .models import car as Car, carDetails as details, flat as Flat, flatDetails as FlatDetails
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile

def main(request):
    now = datetime.datetime.now()
    context = {'carCount':384, 'flatCount':93, 'currentYear':now.year}
    return render(request, 'signup/main.html', context)

def mainUa(request):
    return render(request, 'ua/main.html')

def updFlat(request):
    flat_form = flat()
    if request.user.is_authenticated:
        current_user = User.objects.get(username = request.user.username)
        user_flats = Flat.objects.filter(user = current_user)

        if request.method == 'POST':
            flat_form = flat(request.POST)
            if flat_form.is_valid():

                current_flat_id = request.POST.getlist('flats', None)

                current_flat = Flat.objects.get(id = current_flat_id[0])

                if request.POST.get('warehouse') == 'on':
                    current_flat.warehouse = True
                else:
                    current_flat.warehouse = False

                current_flat.city = request.POST.get('city')
                current_flat.country = request.POST.get('country')
                current_flat.district = request.POST.get('district')
                current_flat.location = request.POST.get('location')

                current_flat.save()

                return redirect('login')
    context = {'flatForm':flat_form, 'flats':user_flats}
    return render(request, 'signup/updFlat.html', context)

def addDetailsFlat(request):
    flat_details_form = flatDetails()
    if request.user.is_authenticated:
        current_user = User.objects.get(username = request.user.username)
        user_flat = Flat.objects.filter(user = current_user)

        if request.method == 'POST':
            flat_details_form = flatDetails(request.POST)
            if flat_details_form.is_valid():
                print('valid')

                current_flat_id = request.POST.getlist('flats', None)
                current_flat = Flat.objects.get(id = current_flat_id[0])

                current_details = FlatDetails.objects.get(flat = current_flat)

                if request.POST.get('smart_tv') == 'on':
                    current_details.smart_tv = True
                else:
                    current_details.smart_tv = False
                if request.POST.get('computer') == 'on':
                    current_details.computer = True
                else:
                    current_details.computer = False
                if request.POST.get('modern_radio') == 'on':
                    current_details.modern_radio = True
                else:
                    current_details.modern_radio = False
                if request.POST.get('conditioner') == 'on':
                    current_details.conditioner = True
                else:
                    current_details.conditioner = False
                if request.POST.get('humidifier') == 'on':
                    current_details.humidifier = True
                else:
                    current_details.humidifier = False
                if request.POST.get('smart_frige') == 'on':
                    current_details.smart_frige = True
                else:
                    current_details.smart_frige = False
                current_details.lights_on_time = request.POST.get('lights_on_time')
                current_details.price = request.POST.get('price')

                current_details.save()
                print('saved')
                return redirect('login')
    context = {'detailsForm':flat_details_form, 'flats':user_flat}
    return render(request, 'signup/flatDetails.html', context)

def addFlat(request):
    flat_form = flat()
    details = flatDetails()

    if request.user.is_authenticated:

        if request.method == 'POST':
            flat_form = flat(request.POST)

            if flat_form.is_valid():

                newflat = flat_form.save(commit=False)

                if request.POST.get('warehouse') == 'on':
                    newflat.warehouse = True
                else:
                    newflat.warehouse = False

                newflat.city = request.POST.get('city')
                newflat.country = request.POST.get('country')
                newflat.district = request.POST.get('district')
                newflat.location = request.POST.get('location')
                newflat.user = request.user

                newflat.save()
                details = details.save(commit=False) # Я еблан, это подтвержденная информация.
                details.flat = newflat
                details.save()

                return redirect('login')
        context = {'flatForm':flat_form, 'flatDetails':details}
        return render(request, 'signup/addFlat.html', context)
    else:
        return redirect('login')


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