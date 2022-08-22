from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.list, name="list"),
    path("create/", views.create, name="create"),
    path("done/", views.done, name="done"),
    path("delete/<str:pk>", views.delete, name="delete"),
]
