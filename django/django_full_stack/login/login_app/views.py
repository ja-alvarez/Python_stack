from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index (request): 
    return render (request, 'index.html')

def home (request):
    if 'user_id' not in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])
    #context = {
    #    'name' : user.first_name #+ ' ' + user.last_name
    #}
    return render(request, 'home.html', {'name': user.first_name}) #context

def register (request):
    form = request.POST
    errors = User.objects.basic_validator(form)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/') 
    user = User.objects.create(first_name = form['first_name'], last_name = form['last_name'], 
    email = form['email'], password = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode())
    request.session['user_id'] = user.id
    return redirect ('/')

def login (request):
    form = request.POST
    try:
        user = User.objects.get(email=form['email'])
    except:
        messages.error(request, 'Check your email and password')
        return redirect ('/')
    if bcrypt.checkpw(form['password'].encode(), user.password.encode()):
        request.session['user_id'] = user.id
    #if form['password'] == user.password:
        #request.session['user_id'] = user.id        
        return redirect ('/homepage')
    messages.error(request, 'Check your email and password')
    return redirect ('/')

def logout(request):
    request.session.clear()
    return redirect('/')