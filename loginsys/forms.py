from django.forms import ModelForm, Textarea, PasswordInput
from loginsys.models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["age", "phone", "email", "country", "photo"]
        labels = {"age": "Age", "phone": "Phone number", "email": "E-mail address", "photo": "Load your photo"}

        widgets = {
            'country': Textarea(attrs={'cols': 55, 'rows': 1}),
            'age': Textarea(attrs={'cols': 55, 'rows': 1}),
            'phone': Textarea(attrs={'cols': 55, 'rows': 1}),
            'email': Textarea(attrs={'cols': 55, 'rows': 1}),
        }