from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.db.models import *
from django.utils.timezone import now


class Authors(Model):
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
        return '\"%s %s\", %s' % (self.first_name, self.last_name, self.year())


class Publisher(Model):
    title = CharField(max_length=32)
    address = TextField()
    city = CharField(max_length=64)
    country = CharField(max_length=64)
    website = URLField()

    def __unicode__(self):
        return '%s (%s, %s)' % (self.title, self.city, self.country)


class Book(Model):
    title = CharField(max_length=128)
    publication_date = DateTimeField(now)
    authors = ManyToManyField(Authors)
    publishers = ForeignKey(Publisher)

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

    def cover_count(self):
        try:
            from bookimgs.models import BooksImage
            count = BooksImage.objects.filter(book_id=self.id).count()
        except:
            count = 0
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
                    "cover_count",
                    "loaded_images_total"]
    list_display_links = ("title",)
    ordering = ("id",)
    inlines = [BooksInline, ]
