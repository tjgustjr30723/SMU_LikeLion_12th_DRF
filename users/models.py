from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.utils import timezone
class User(AbstractUser):
    #user = models.CharField(max_length=50)
    #password = models.CharField(max_length=100, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    #email = models.EmailField(max_length = 254, unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    sign_up_at = models.DateTimeField(default=timezone.now())
    old = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=None, null=True, blank=True)
    height = models.IntegerField(validators=[MinValueValidator(0)], default=None, null=True, blank=True)
    weight = models.IntegerField(validators=[MinValueValidator(0)], default=None, null=True, blank=True)


