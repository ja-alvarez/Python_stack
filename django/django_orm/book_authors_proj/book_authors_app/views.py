from django.shortcuts import render, redirect
from .models import Book, Author

def index (request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'createbook.html', context)


def add_book (request):
    #Book.objects.create(title=request.POST['newbookname'], desc=request.POST['newbookdesc'])
#    return redirect('/')
    form = request.POST
    Book.objects.create(
        title = form ['newbookname'],
        description = form['newbookdesc']
    )
    return redirect('/')

def all_authors(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, 'createauthor.html', context)

def add_author (request):
    form = request.POST
    Author.objects.create(
    first_name = form ['newauthorname'], 
    last_name = form ['newauthorlastname'], 
    notes = form ['newauthornotes']   
    )
    return redirect('authors/')
    
def books (request, book_id):
    context = {
        'books': Book.objects.get(id=book_id),
        'authors': Author.objects.all()
    }
    return render (request, 'showbook.html', context)

def add_author_to_book (request, book_id):
    this_book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    this_book.authors.add(author)
    #return redirect('/')
    return redirect (f'/books/{book_id}')

def authors(request, author_id):
    context = {
        'authors': Author.objects.get(id=author_id),
        'books': Book.objects.all()
    }   
    return render (request, 'showauthor.html', context)

def add_book_to_author (request, author_id):
    this_author = Author.objects.get(id=author_id)
    book = Books.objects.get(id=request.POST['book_id'])

    this_author.books.add(book)
    return redirect (f'/authors/{author_id}')
    #return redirect('/')









