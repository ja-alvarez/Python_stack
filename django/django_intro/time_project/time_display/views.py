from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index (request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p")
    }
    return render (request, 'index.html', context)