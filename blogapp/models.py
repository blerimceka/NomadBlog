from django.db import models

# Create your models here.

import datetime
from django.utils import timezone


class Post(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    upload = models.ImageField(upload_to='images/')
    intro = models.CharField(max_length=400)
    body = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
