from django.contrib import admin
from . import models
from .views import register
# Register your models here.

admin.site.register(models.Albums)
admin.site.register(models.song)