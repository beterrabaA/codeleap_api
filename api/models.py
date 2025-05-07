import datetime

from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    created_datetime = models.DateTimeField()

    def __str__(self):
        return self.username
