from django.shortcuts import render, redirect
from random import random, randint, uniform
from time import strftime, localtime

time = strftime("%b %d, %Y %H:%M %p", localtime())

def index (request):
    request.session['gold'] = 0
    request.session['output'] = [] #append = []
    return render (request, 'index.html')

def process_money(request):
    gold = request.session['gold']
    output = request.session['output']
    message= ""
    if request.POST['opcion'] == "farm":
        val = randint(10, 20)
        gold = gold + val
        message = (f"Earned {val} from {request.POST['opcion']}! ({time})") 
        output.append(message)

    elif request.POST['opcion'] == "cave":
        val = randint(5,10)
        gold= gold + val 
        message = (f"Earned {val} from {request.POST['opcion']}! ({time})")
        output.append(message)

    elif request.POST['opcion'] == "house":
        val = randint(2, 5)
        gold = gold + val
        message = (f"Earned {val} from {request.POST['opcion']}! ({time})")
        output.append(message)

    elif request.POST['opcion'] == "casino":
        val = randint (-50, 50)
        gold= gold + val
        if val <0:
            message = (f"Lost {val} from {request.POST['opcion']}... Ouch...({time})")
            output.append(message)
        else:
            message = (f"Earned {val} from {request.POST['opcion']}! ({time})")
            output.append(message)
            
    request.session['gold'] = gold
    return render (request,'index.html')

def reset (request):
    request.session['gold'] = 0
    request.session['output'] = ''
    return render (request, 'index.html')