from django.urls import path

from . import views
app_name = 'travello'

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("contact", views.contact, name="contact"),
]
