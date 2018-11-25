from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_title, name='main_title'),
    path("books/", views.books_title, name='book_title'),
    path("authors/", views.authors_title, name='authors_title'),
    path("books/<str:book_name>/", views.book_title, name='book_title'),
    path("authors/<str:author>/", views.author_title, name='author_title')
]
