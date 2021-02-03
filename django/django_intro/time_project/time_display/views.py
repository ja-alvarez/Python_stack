from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index (request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p")
    }
    return render (request, 'index.html', context)

# "time": strftime("%b %d, %Y %H:%M %p", gmtime())

#    <h1>{{time.strftime("%b %d, %Y") <br>
 #       time.strftime("%H:%M %p"}}</h1>