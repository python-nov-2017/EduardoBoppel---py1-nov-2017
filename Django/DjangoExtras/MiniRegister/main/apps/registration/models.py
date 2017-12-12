from __future__ import unicode_literals
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 50, validators=[RegexValidator(regex='^[a-zA-Z]{2,}$', message='Field must be mimimum 2 characters and only letters', code='invalid_username'),])
    last_name = models.CharField(max_length = 50, validators=[RegexValidator(regex='^[a-zA-Z]{2,}$', message='Field must be mimimum 2 characters and only letters', code='invalid_username'),])
    email = models.EmailField(max_length = 50, unique=True)
    password = models.CharField(max_length = 50, validators=[MinLengthValidator(8)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
