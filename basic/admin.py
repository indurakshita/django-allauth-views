from django.contrib import admin
from .models import PersonModel

class PersonAdmin(admin.ModelAdmin):
    
    admin.site.register(PersonModel)