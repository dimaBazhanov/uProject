from django.contrib import admin
from .models import Profile, userPreferences, car, carDetails

# Register your models here.
admin.site.register(Profile)
admin.site.register(userPreferences)
admin.site.register(car)
admin.site.register(carDetails)