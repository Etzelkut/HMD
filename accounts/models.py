from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, default=0)
    sex = models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female')], blank=True)
    weight = models.PositiveIntegerField(blank=True, default=0)
    height = models.PositiveIntegerField(blank=True, default=0)
    allergia = models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3)
    xray = models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no'), ('did not check', 'did not check')], max_length=15)
    habbits = models.CharField(max_length=6, blank=True, choices=[('smoke', 'smoke'), ('drink', 'drink')])
    def __str__(self):
        return self.username
