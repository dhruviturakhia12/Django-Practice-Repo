from django.urls import path
from .views import HomeView,DeleteView,AddView
urlpatterns = [
   path("",HomeView.as_view(),name="home"),
   path('delete/<int:id>/', DeleteView.as_view(), name="delete"),
   path("add/", AddView.as_view(), name="add"),

]
