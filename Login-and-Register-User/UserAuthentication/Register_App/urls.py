from django.contrib import admin
from django.urls import path,include
from Register_App.views import Registration
urlpatterns = [
    path('register/', Registration, name='register'),
]