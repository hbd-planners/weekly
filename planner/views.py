from django.shortcuts import render
from .utils import get_current_week_range

def home(request):
    
    context = {
        'current_week': get_current_week_range, 
    }

    return render(request, 'home.html', context) 


