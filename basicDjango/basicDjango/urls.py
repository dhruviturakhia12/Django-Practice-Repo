from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('travello',include('travellersGuide.urls')),
    path('admin/', admin.site.urls),
]
