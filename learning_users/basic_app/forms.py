from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# This is the build in User model.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


# This is the stuff we added to the User model.
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
