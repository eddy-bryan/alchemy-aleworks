from django.urls import path
from . import views

urlpatterns = [
    path('beers/', views.beers, name='beers'),
    path('merch/', views.merch, name='merch'),
    path('search/', views.search_view, name='search'),
    path('beers/<int:beer_id>/', views.beer_detail, name='beer_detail'),
    path('merch/<int:merch_id>/', views.merch_detail, name='merch_detail'),
    path('add_beer/', views.add_beer, name='add_beer'),
    path('add_merch/', views.add_merch, name='add_merch'),
    path('edit_beer/<int:beer_id>/', views.edit_beer, name='edit_beer'),
    path('edit_merch/<int:merch_id>/', views.edit_merch, name='edit_merch'),
]
