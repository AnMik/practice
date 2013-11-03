from django.contrib import admin
from django.db.models import *
from library.settings import MEDIA_ROOT
from books.models import Book


class BooksImage(Model):
    image_thumbnail = ImageField(upload_to="bookimgs/images/thumbnails/")
    image_full = ImageField(upload_to="bookimgs/images/fulls/",
                            null=True,
                            blank=True)
    book_id = ForeignKey(Book, blank=True, null=True)

    def images_count_simple(self):
        count = 0
        if self.image_thumbnail:
            count += 1
        if self.image_full:
            count += 1
        return count

    def __unicode__(self):
        return "%s" % self.id

    def image_preview(self):
        return '<img src="%s%s"/>' % (MEDIA_ROOT, self.image_thumbnail.name)
    image_preview.allow_tags = True


class BooksImageAdmin(admin.ModelAdmin):
        list_display = ["id", "image_preview", "images_count_simple"]
        ordering = ("id",)
