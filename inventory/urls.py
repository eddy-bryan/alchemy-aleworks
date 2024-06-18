from django.urls import path
from . import views

urlpatterns = [
    path('beers/', views.beers, name='beers'),
    path('merch/', views.merch, name='merch'),
    path('beers/<beer_id>/', views.beer_detail, name='beer_detail'),
    path('merch/<merch_id>/', views.merch_detail, name='merch_detail'),
]
