from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, template, context)

def one_book(request, some_book):
    some_book == Book.pub_date
    template = 'books/one_book.html'
    books = Book.objects.all()
    context = {"books" : books}
    return render(request,template,context)
