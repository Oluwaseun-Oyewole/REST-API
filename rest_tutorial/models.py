
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.CharField(max_length=100, default=False)
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'
