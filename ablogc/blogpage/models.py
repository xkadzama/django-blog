from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime


class Category(models.Model):
    name_category = models.CharField(max_length=150)


    def __str__(self) -> str:
        return self.name_category

    def get_absolute_url(self):
        return reverse('home-page')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=255, default='other')
    post_date = models.DateField(auto_now_add=True)
    post_date_time = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title + ' @' + str(self.author)


    def get_absolute_url(self):
        return reverse('home-page')

