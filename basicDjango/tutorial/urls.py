from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('sub', views.sub, name='sub'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
]