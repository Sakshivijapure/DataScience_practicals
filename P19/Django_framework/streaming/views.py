from django.shortcuts import render
from .models import NetflixShow

def netflix_list(request):
    shows = NetflixShow.objects.all()  # Fetch all shows
    return render(request, 'streaming/netflix_list.html', {'shows': shows})

