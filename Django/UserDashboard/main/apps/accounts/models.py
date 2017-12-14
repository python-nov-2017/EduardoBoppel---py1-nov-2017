from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff=False, is_admin=False, is_superuser=False, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff = is_staff,
            is_admin = is_admin,
            is_superuser = is_superuser,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(email, password, **kwargs)
    
    def create_staffuser(self, email, password, **kwargs):
        return self._create_user(email, password, True, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, True, True, True, **kwargs)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def get_user_level(self):
        if self.is_admin:
            return "Admin User"
        return "Normal User"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def get_absolute_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.pk})

    def get_messages_url(self):
        return reverse('messages:message_list', kwargs={'pk': self.pk})

    # @property
    # def is_active(self):
    #     return self.is_active

    # @property
    # def is_staff(self):
    #     return self.is_staff

    # @property 
    # def is_admin(self):
    #     return self.is_admin

    