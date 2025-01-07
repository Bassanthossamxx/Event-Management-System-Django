from django.shortcuts import render , redirect
# Create your views here.
from .models import Event
def displayEvents(request):
    events = Event.objects.all()
    return render(request, 'base/home.html', {'events': events})

