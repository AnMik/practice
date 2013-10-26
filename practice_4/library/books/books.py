from books.models import Book
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render


def get_all(request):
    books = get_all_books()
    return render(request, "books.html", {'books': books})


def get_one(request, book_id):
    book = get_one_book(book_id)
    return render(request, "one_book.html", {'book': book})


def get_all_books():
    return Book.objects.all()


def get_one_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
    except ObjectDoesNotExist:
        return "No book with that id"
    except MultipleObjectsReturned:
        return "Several unique id's, wat?"
    return book
