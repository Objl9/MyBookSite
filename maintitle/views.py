from django.http import HttpResponse
from django.shortcuts import render
from .models import Books, Authors


def main_title(request):
    return render(request, "main_title.html")


def books_title(request):
    books = Books.objects.all()
    context = {"books": books}
    return render(request,"books_title.html",context)


def authors_title(request):
    authors = Authors.objects.all()
    context = {"authors":authors}
    return  render(request,"authors_title.html", context)


def book_title(request, book_name):
    book = Books.objects.get(book_name=book_name)
    context = {"book_name": book.book_name, "book_author": book.author,
               "book_description": book.description}
    return render(request, "book_title.html", context)


def author_title(request,author):
    author = Authors.objects.get(author=author)
    books = Books.objects.filter(author=author)
    context = {'author': author.author, "books": books, "author_description": author.description}
    return render(request, "author_title.html", context)
