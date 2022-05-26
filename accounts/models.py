from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(blank=True, null=True)
    is_vip = models.BooleanField(default=False)
    vip_end_time = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)