from django.http import JsonResponse
from django.shortcuts import render
from .models import ClickCounter
from datetime import datetime

def index(request):
    # Fetch the current click count or initialize it if it doesn't exist
    counter, created = ClickCounter.objects.get_or_create(id=1)
    return render(request, 'counter.html', {'numClicks': counter.count,})

def increment_counter(request):
    # Increment the click count in the database
    counter, created = ClickCounter.objects.get_or_create(id=1)
    counter.count += 1
    counter.save()
    return JsonResponse({'numClicks': counter.count})

def save_counter(request):
    # Save the click count in the database
    counter, created = ClickCounter.objects.get_or_create(id=1)
    counter.save()
    return JsonResponse({'numClicks': counter.count})

