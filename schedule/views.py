from django.shortcuts import render
from django.http import JsonResponse
from .models import Event


def Calendar(request):

    return render(request, 'schedule/calendar.html')




def get_events(request):
    events = Event.objects.all()
    event_list = [
        {
            "title": event.title,
            "start": event.start_time.isoformat(),
            "end": event.end_time.isoformat(),
        }
        for event in events
    ]
    return JsonResponse(event_list, safe=False)



    