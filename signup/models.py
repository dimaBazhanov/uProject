from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    company = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    companySpec = models.IntegerField(null=True, blank=True,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ])

class userPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    humidity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    temperature = models.DecimalField(max_digits=10, decimal_places=2, default=25)
    displayStartPage = models.CharField(max_length=254, default='google.com')
    radioWave = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tvChannel = models.IntegerField(null=True, blank=True)
    frigeTemperature = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    id = models.AutoField(primary_key=True, help_text="Unique ID for this particular car")
    mark = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    county = models.CharField(max_length=254) # Опечатка вышла, потом исправлю
    location = models.CharField(max_length=254)

    

class carDetails(models.Model):
    car = models.OneToOneField(car, on_delete=models.CASCADE)

    radio = models.BooleanField(default=False)
    display = models.BooleanField(default=False)
    airConditioner = models.BooleanField(default=False)
    glassFogging = models.BooleanField(default=False)
    inside = models.CharField(max_length=255, default='dummy text')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lights = models.BooleanField(default=False) # Если True то ксенон. фары если False - обчные
    colour = models.CharField(max_length=6, default='ffffff') # Сделать все поля обязательными к заполнению в обоих таблицах

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        userPreferences.objects.create(user=instance)
        #carvar = car.objects.create(user=instance)
        #carDetails.objects.create(car=carvar)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()