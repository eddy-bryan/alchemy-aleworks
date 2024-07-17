from django.urls import path
from . import views

urlpatterns = [
    path('taproom/', views.taproom, name='taproom'),
    path('about/', views.about, name='about'),
    path(
        'orders_and_returns/',
        views.orders_and_returns,
        name='orders_and_returns'
    ),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path(
        'terms_and_conditions/',
        views.terms_and_conditions,
        name='terms_and_conditions'
    ),
]
