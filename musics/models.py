from django.db import models
from django.db import models
from django.db.models.fields import FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from .templates import *

# Create your models here.
class Albums(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    logo = models.CharField(max_length=99999)
    logo_file = models.FileField()

    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title + ' - ' + self.artist

class song(models.Model):
    album = ForeignKey(Albums, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    length = models.FloatField(null=True)
    is_favorite = models.BooleanField(default=False)
    path = models.FileField(upload_to='media/%y')
    duration = models.FloatField()

    def __str__(self):
        return self.name + ' - ' + str(self.is_favorite)
    