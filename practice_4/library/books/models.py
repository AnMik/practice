from django.db.models import *
from django.utils.safestring import mark_safe
from django.utils.timezone import now


class Authors(Model):
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    email = EmailField(null=True, blank=True)

    def __unicode__(self):
        return '\"%s %s\"' % (self.first_name, self.last_name)


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
        authors = ["<a href=authors/" + str(a.id) + ">" +
                   a.__unicode__() +
                   "</a>" for a in self.authors.all()]
        publishers = self.publishers.__unicode__()
        return '\"%s\" %s, \n%s,  \n%s' % \
               (self.title, self.publication_date, authors, publishers)
