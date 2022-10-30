from django.contrib import admin
from django.db import models
from django.contrib.admin import ModelAdmin
# Create your models here.

class LocalUsers(models.Model):
    UserName = models.SlugField()
    Password = models.SlugField()
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.SlugField()
    last_login = ''

    class View(admin.ModelAdmin):
        list_display = ['UserName','Email']

    def __str__(self):
        return self.UserName
    

