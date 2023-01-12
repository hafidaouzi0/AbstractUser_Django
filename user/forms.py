from django import forms
from .models import NewUser



class NewUserForm(forms.ModelForm):
    class Meta:
        model=NewUser
        fields=["first_name","last_name","nickname","age"]