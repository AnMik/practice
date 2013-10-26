from django.conf.urls import patterns, url


urlpatterns = patterns(
    'books.books',
    url(r'^lib/$', 'get_all'),
    url(r'^lib/(?P<book_id>\d+)/?$', 'get_one'),
)


urlpatterns += patterns(
    'books.authors',
    url(r'^lib/authors/$', 'get_all'),
    url(r'^lib/authors/(?P<author_id>\d+)/?$', 'get_one'),
)
