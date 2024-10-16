from django.http import JsonResponse
from django.shortcuts import render
from .models import ClickCounter
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json

def index(request):
    # Fetch the current click count or initialize it if it doesn't exist
    counter, created = ClickCounter.objects.get_or_create(id=1)
    return render(request, 'counter.html', {'numClicks': counter.count})

@csrf_exempt
def save_counter(request):
    # Save the click count in the database
    if request.method == 'POST':
        data = json.loads(request.body)
        click_count = data.get('numClicks', 1)  # Retrieves the click count
        date = data.get('date', timezone.now().date())  # Retrieves the date or defaults to today
        time = data.get('time', timezone.now().time())  # Retrieves the time or defaults to now

        counter = ClickCounter(count=click_count, date=date, time=time)
        counter.save()  # Save the new entry
        
        return JsonResponse({'numClicks': counter.count, 'date': str(counter.date), 'time': str(counter.time)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
