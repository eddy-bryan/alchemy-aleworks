# pages/views.py
from django.shortcuts import render

def taproom(request):
    """ Render the Taproom page. """
    return render(request, 'pages/taproom.html')

def about(request):
    """ Render the About page. """
    return render(request, 'pages/about.html')
