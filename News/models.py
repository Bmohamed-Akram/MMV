from this import d
from django.db import models
from datetime import datetime
# Create your models here.

now = datetime.now()

class News(models.Model):
    title = models.CharField(max_length=100)
    img_news = models.ImageField()
    dt = models.DateTimeField(default=now , blank=True)
    body = models.CharField(max_length=3000)