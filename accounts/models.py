from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('provider', 'Provider'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username