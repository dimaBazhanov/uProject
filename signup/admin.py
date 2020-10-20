from django.contrib import admin
from .models import Profile, userPreferences

# Register your models here.
admin.site.register(Profile)
admin.site.register(userPreferences)