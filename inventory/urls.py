from django.urls import path
from . import views

urlpatterns = [
    path('beers/', views.beers, name='beers'),
    path('merch/', views.merch, name='merch'),
    path('<beer_id>/', views.beer_detail, name='beer_detail'),
]
