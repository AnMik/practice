from django.contrib import admin
from django.db.models import *
from imgs.settings import MEDIA_ROOT
from books.models import Book


class BooksImage(Model):
    image_thumbnail = ImageField(upload_to="bookimgs/images/thumbnails/")
    image_full = ImageField(upload_to="bookimgs/images/fulls/",
                            null=True,
                            blank=True)
    book_id = ForeignKey(Book, blank=True, null=True)

    def images_count(self):
        """ ТруЪ-метод подсчета
        Получаем все поля текущей модели, извлекаем имена,
        получаем соответствующие именам атрибуты, берем ненулевые и считаем
        количество путем вычисления суммы. Двойку вычитаем,
        так как поле идентификатора и поле ключа учитывать не надо
        """
        return sum(not not v
                   for v in [getattr(self, f.name)
                             for f in self._meta.fields]) - 2

    def images_count_simple(self):
        """ Метод подсчета для слабаков
        Вручную проверяем все поля
        """
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
    list_display = ["id", "image_preview", "images_count"]
    ordering = ("id",)
