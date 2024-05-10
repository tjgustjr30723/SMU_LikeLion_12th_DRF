from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.utils import timezone
class User(AbstractUser):
    email = models.EmailField(max_length = 254, unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    sign_up_at = models.DateTimeField(auto_now_add=True)
    old = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=0)
    height = models.IntegerField(validators=[MinValueValidator(0)], null=True, default=0)
    weight = models.IntegerField(validators=[MinValueValidator(0)], default=0)


