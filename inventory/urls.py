from django.urls import path
from . import views

urlpatterns = [
    path('beers/', views.beers, name='beers'),
]
