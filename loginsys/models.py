from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        db_table = "user_profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.TextField(blank=True, null=True, verbose_name="Age")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone number")
    email = models.EmailField(verbose_name="E-mail address")
    country = models.TextField(blank=True, null=True, verbose_name="From")
    photo = models.ImageField(null=True, blank=True, upload_to='users_photo/', verbose_name='Avatar')

