from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path,include
from Register_App.views import Registration
urlpatterns = [
    path('login/',obtain_auth_token,name="login"),
    path('register/', Registration, name='register'),
]