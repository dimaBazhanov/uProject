from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    company = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)

class userPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    humidity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    temperature = models.DecimalField(max_digits=10, decimal_places=2, default=25)
    displayStartPage = models.CharField(max_length=254, default='google.com')
    radioWave = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tvChannel = models.IntegerField(null=True, blank=True)
    frigeTemperature = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        userPreferences.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()