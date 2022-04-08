from asyncio.windows_events import NULL
from operator import mod
from django.db import models
from datetime import datetime

# Create your models here.
now = datetime.now()

class images(models.Model):
    dt = models.DateTimeField(default=now,blank= True)
    picture = models.ImageField()
    #about = models.CharField(max_length=100, default= NULL)
    title = models.CharField(max_length=100)