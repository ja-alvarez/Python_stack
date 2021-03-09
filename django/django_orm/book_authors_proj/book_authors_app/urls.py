from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('authors/', views.all_authors),
    path('add_author', views.add_author),
    path('books/<int:book_id>', views.books),
    path ('add_author_to_book/<int:book_id>', views.add_author_to_book),
    path('authors/<int:author_id>', views.authors),
    path('add_book_to_author/<int:author_id>', views.add_book_to_author),
]