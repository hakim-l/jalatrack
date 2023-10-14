from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import EmployeeModel
from .forms import CustomUserChangeForm,customUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = customUserCreationForm
    form= CustomUserChangeForm
    model= EmployeeModel
    list_display = ['email','username']

admin.site.register(EmployeeModel,CustomUserAdmin)