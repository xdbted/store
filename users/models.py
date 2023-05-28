from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
