from django.urls import path
from . import views

urlpatterns = [
    path('taproom/', views.taproom, name='taproom'),
    # path('about/', views.about, name='about'),
]
