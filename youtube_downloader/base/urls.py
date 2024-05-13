from django.http import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("download/<path:url>/<str:name>/<str:type>l", views.download_file, name='download')
]