from rest_framework.routers import DefaultRouter
from employee.views import SignUpView, LoginView
from django.urls import path

urlpatterns=[
    path('signup/',SignUpView.as_view(),name= 'signup'),
    path('login/',LoginView.as_view(), name= 'login')
]
