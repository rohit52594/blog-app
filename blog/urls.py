from django.contrib import admin
from django.urls import path
from .views import home, about, contact, login, register, privacy, userRegister

urlpatterns = [
    path('', home, name = "home"),
    path('about/', about, name = "about"),
    path('contact/', contact, name = "contact"),
    path('login/', login, name = "login"),
    path('register/', register, name = "register"),
    path('privacy-policy/', privacy, name = "privacy"),
    path('userRegister/', userRegister, name = "userRegister"),
]
