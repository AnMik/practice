from books.models import Authors
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render


def get_all(request):
    authors = get_all_authors()
    return render(request, "authors.html", {'authors': authors})


def get_one(request, author_id):
    author = get_one_author(author_id)
    return render(request, "one_author.html", {'author': author})


def get_all_authors():
    return Authors.objects.all()


def get_one_author(author_id):
    try:
        author = Authors.objects.get(id=author_id)
    except ObjectDoesNotExist:
        return "No author with that id"
    except MultipleObjectsReturned:
        return "Several unique id's, wat?"
    return author
