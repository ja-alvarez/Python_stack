from django.shortcuts import render, HttpResponse,redirect
#from django.http import jsonResponse

def root (request):
    return redirect('/blogs')

def index (request):
    return HttpResponse ('INDEX marcador de posición para luego mostrar una lista de todos los blogs')

def new (request):
    return HttpResponse(' NEW marcador de posición para mostrar un nuevo formulario para crear un nuevo blog')

def create (request):
    return redirect ('/')

def show (request, _number):
    return HttpResponse(f'SHOW marcador de posición para mostrar el blog numero: {int(_number)}')

def edit (request, _number):
    return HttpResponse(f'EDIT marcador de posición para editar el blog {int(_number)}')

def destroy (request, _number):
    return redirect('/blogs')

#def json (request):
#    return json.dumps('content')