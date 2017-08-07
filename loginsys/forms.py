from django.forms import ModelForm
from loginsys.models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["user_phone", "user_email", "user_bio", "user_photo"]
        labels = {"user_phone": "Phone number", "user_email": "E-mail address", "user_photo": "Load your photo"}
        help_text = {"user_phone": "Enter your cell-phone number", "user_email": "E-mail address"}