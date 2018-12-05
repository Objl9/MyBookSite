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


def book_title(request, id_book):
    book = Books.objects.get(id_book=id_book)
    author = Authors.objects.get(author = book.author)
    context = {"book_name": book.book_name, "book_author": book.author,
               "book_description": book.description, "id_author": author.id_author}
    return render(request, "book_title.html", context)


def author_title(request,id_author):
    author = Authors.objects.get(id_author=id_author)
    books = Books.objects.filter(author=author)
    context = {'author': author.author, "books": books, "author_description": author.description}
    return render(request, "author_title.html", context)
