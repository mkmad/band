from django import forms
from models import UserProfile

# Creating a form from the django models.
class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)