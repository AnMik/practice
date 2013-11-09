from django.views.generic import ListView, DetailView
from django.contrib import admin
from django.db.models import *
from django.shortcuts import render_to_response
from library.settings import MEDIA_ROOT
from books.models import Book
from utils.models import TimeStampedModel


class BooksImage(TimeStampedModel):
    image_thumbnail = ImageField(upload_to="bookimgs/images/thumbnails/")
    image_full = ImageField(upload_to="bookimgs/images/fulls/",
                            null=True,
                            blank=True)
    book_id = ForeignKey(Book, blank=True, null=True)

    def images_count(self):
        count = 0
        if self.image_thumbnail:
            count += 1
        if self.image_full:
            count += 1
        return count

    def __unicode__(self):
        return "%s" % self.id

    def image_preview(self):
        return render_to_response("pic_url.html",
                                  {'folder': MEDIA_ROOT,
                                   'image': self.image_thumbnail.name}).content
    image_preview.allow_tags = True


class BooksImageAdmin(admin.ModelAdmin):
        list_display = ["id",
                        "image_preview",
                        "images_count",
                        "created",
                        "updated"]
        ordering = ("id",)


class BooksImageList(ListView):
    model = BooksImage
    paginate_by = 2
    template_name = 'booksimage_list.html'


class BooksImageDetail(DetailView):
    model = BooksImage

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if queryset is None:
            queryset = self.get_queryset()

        if pk is not None:
            queryset = queryset.filter(pk=pk)
        obj = queryset.get()

        return obj
