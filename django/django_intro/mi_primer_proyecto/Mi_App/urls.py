from django.urls import path
from . import views
urlpatterns = [

    path('', views.root), #cd = /
    path('blogs/', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:_number>', views.show),
    path('blogs/<int:_number>/edit', views.edit),
    path('blogs/<int:_number>/delete', views.destroy), #hacer que _number solo acepte INT
#    path('blogs/json', views.json)
]