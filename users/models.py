from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    email = models.EmailField(
        max_length=127,
        unique=True,
        error_messages={
            'unique': 'This field must be unique.'
        }
    )

    username = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': 'A user with that username already exists.'
        }
    )