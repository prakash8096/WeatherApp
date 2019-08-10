from django.db import models
from django.utils import timezone

# Create your models here.
class City(models.Model):
    city=models.CharField(max_length=20)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.city


    
