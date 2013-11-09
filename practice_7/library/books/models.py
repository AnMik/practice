from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.db.models import *
from django.utils.timezone import now
from django.views.generic import ListView, DetailView
from utils.models import TimeStampedModel


class Authors(TimeStampedModel):
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    email = EmailField(null=True, blank=True)
    birthyear = SmallIntegerField(null=True, blank=True)

    def year(self):
        year = self.birthyear
        if not year:
            year = "возраст неизвестен"
        print(year)
        return year

    def __unicode__(self):
        return "\"{} {}\", {}".format(self.first_name,
                                      self.last_name,
                                      self.year())


class Publisher(TimeStampedModel):
    title = CharField(max_length=32)
    address = TextField()
    city = CharField(max_length=64)
    country = CharField(max_length=64)
    website = URLField()

    def __unicode__(self):
        return "{} ({}, {})".format(self.title, self.city, self.country)


class Book(TimeStampedModel):
    title = CharField(max_length=128)
    publication_date = DateTimeField(now)
    authors = ManyToManyField(Authors)
    publishers = ForeignKey(Publisher)
    description = TextField()

    def get_absolute_url(self):
        return self.id

    def __unicode__(self):
        return '\"%s\"' % self.title

    def book_authors(self):
        return ', '.join([author.first_name for author in self.authors.all()])

    def loaded_images_total(self):
        count = 0
        try:
            from bookimgs.models import BooksImage
            for cover in BooksImage.objects.filter(book_id=self.id):
                count += cover.images_count()
        except:
            pass
        return count


class BooksInline(admin.TabularInline):
    from bookimgs.models import BooksImage
    model = BooksImage
    extra = 1


class BookAdmin(ModelAdmin):
    list_display = ["id",
                    "title",
                    "book_authors",
                    "publishers",
                    "loaded_images_total"]
    list_display_links = ("title",)
    ordering = ("id",)
    inlines = [BooksInline, ]


class BooksList(ListView):
    model = Book
    paginate_by = 2
    template_name = 'books_list.html'


class BooksDetail(DetailView):
    model = Book

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if queryset is None:
            queryset = self.get_queryset()

        if pk is not None:
            queryset = queryset.filter(pk=pk)
        obj = queryset.get()

        return obj
