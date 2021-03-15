from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import NewCourse

def index (request):
    all_courses = NewCourse.objects.all()
    context = {
        'all_courses' : all_courses
    }
    return render(request, 'index.html', context)

def create (request):
    errors = NewCourse.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        NewCourse.objects.create(name = request.POST['name'], description = request.POST['description'])
        messages.success(request, "Course successfully created")
        return redirect('/')

def destroy(request, id):
    context = {
        "course": NewCourse.objects.get(id=id)
    }
    return render(request, 'delete.html', context)

def delete(request, id):
    NewCourse.objects.get(id=id).delete()
    return redirect('/')
    

