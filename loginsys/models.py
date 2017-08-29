from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        db_table = "user_profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone number")
    user_email = models.EmailField(verbose_name="E-mail address")
    user_bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    user_photo = models.ImageField(null=True, blank=True, upload_to='users_photo/', verbose_name='Avatar')
