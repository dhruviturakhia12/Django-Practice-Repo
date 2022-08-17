from django.contrib import admin
from django.urls import path
from . import views as poll_views

urlpatterns = [
    path("", poll_views.index, name="index"),
    path("home/", poll_views.home, name="home"),
    path("create/", poll_views.create, name="create"),
    path("vote/<poll_id>/", poll_views.vote, name="vote"),
    path("results/<poll_id>/", poll_views.results, name="results"),
]
