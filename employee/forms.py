from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import EmployeeModel


class customUserCreationForm(UserCreationForm):
    class Meta:
        model= EmployeeModel
        fields= ('username','email','password')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = EmployeeModel
        fields = ("username", "email")