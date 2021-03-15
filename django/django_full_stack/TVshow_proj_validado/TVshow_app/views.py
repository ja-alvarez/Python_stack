from django.shortcuts import render, redirect
from .models import Tvshow
from time import strftime, strptime
from django.contrib import messages

def home(request):
    return redirect('/shows')

def index(request):
    new_show= Tvshow.objects.all()
    context = {
        'new_show': new_show
    }
    return render(request, 'index.html', context)

def new_show(request):
    return render(request, 'addshow.html')

def create_show(request):
    errors = Tvshow.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        new_show = Tvshow.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        messages.success(request, 'TV show successfully created')
        return redirect(f'/shows/{new_show.id}')

def show_info(request, show_id):
    show = Tvshow.objects.get(id=show_id)
    context = {
        'show': show
    }
    return render(request, 'show_info.html', context)

def edit_show(request, show_id):
    editshow = Tvshow.objects.get(id=show_id)
    context = {
        'editshow': editshow
    }
    return render(request, 'edit_show.html', context)

def update_show(request, show_id):
    errors = Tvshow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('shows/{updateshow.id}') 
    else:
        updateshow = Tvshow.objects.get(id=show_id)
        updateshow.title = request.POST['title']
        updateshow.network = request.POST['network']
        updateshow.release_date = request.POST['release_date']
        updateshow.description = request.POST['description']
        updateshow.save()
        messages.success(request, 'TV show successfully updated')
        return redirect(f'/shows/{updateshow.id}')

def delete_show(request, show_id):
    delshow = Tvshow.objects.get(id=show_id)
    delshow.delete()
    return redirect('/shows')