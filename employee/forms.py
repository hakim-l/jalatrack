from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import EmployeeModel
from division.models import DivisionModel

class customUserCreationForm(UserCreationForm):
    class Meta:
        model= EmployeeModel
        fields= ('username','email','first_name','last_name',
       'division', 'is_supervisor',)
        division= forms.ModelChoiceField(queryset=DivisionModel.objects.all()
                                         )




class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = EmployeeModel
        fields = ("email",)
#