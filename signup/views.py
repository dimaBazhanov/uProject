from django.contrib.auth import login as auth_login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

from .models import Profile
def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form' : form}
    return render(request, 'signup/signup.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('user')
    return render(request, 'signup/login.html')

def showUser(request):

    return render(request, 'signup/aboutUser.html')



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