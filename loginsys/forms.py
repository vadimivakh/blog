from django.forms import ModelForm, Textarea, PasswordInput
from loginsys.models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["user_age", "user_phone", "user_email", "user_country", "user_photo"]
        labels = {"user_age": "Age", "user_phone": "Phone number", "user_email": "E-mail address", "user_photo": "Load your photo"}

        widgets = {
            'user_country': Textarea(attrs={'cols': 55, 'rows': 1}),
            'user_age': Textarea(attrs={'cols': 55, 'rows': 1}),
            'user_phone': Textarea(attrs={'cols': 55, 'rows': 1}),
            'user_email': Textarea(attrs={'cols': 55, 'rows': 1}),
        }