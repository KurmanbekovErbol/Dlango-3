from django.urls import path
from main.views import banners

urlpatterns = [
    path('', banners, name='banner'),
]