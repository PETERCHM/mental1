# yourapp/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'landing.html')

def forums(request):
    return render(request, 'forums.html')

# Add more views as needed
