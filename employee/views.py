from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserChangeForm, customUserCreationForm

# Create your views here.

class employeeView(TemplateView):
    template_name = '/dashboard/employee.php'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context.update({'c':''})


class SignUpView(CreateView):
    form_class = customUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    # def post(self, request, *args, **kwargs):
    #     return

class LoginView(CreateView):
    # form_class = custom
    success_url = reverse_lazy("login")
    template_name = "registration/login.html"
    def post(self, request, *args, **kwargs):
        return

