from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("password-done/", views.password, name="password"),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='password.html',success_url='/password-done/'),name='change_password'),
]
