from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookimgs.models import BooksImageList, BooksImageDetail
from books.models import BooksList, BooksDetail
from registration import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^booksimage/list/(?P<page>\d+)/$', BooksImageList.as_view()),
    url(r'^booksimage/details/(?P<pk>\d+)/$', BooksImageDetail.as_view(
        template_name="booksimage_detail.html")),

    url(r'^books/list/(?P<page>\d+)/$', BooksList.as_view()),
    url(r'^books/details/(?P<pk>\d+)/$', BooksDetail.as_view(
        template_name="books_detail.html")),

    url(r'^accounts/login/$', views.login),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid_login/$', views.invalid_login),
    url(r'^accounts/register/$', views.register),
    url(r'^accounts/register_success/$', views.register_success),
    url(r'^accounts/register_failed/$', views.register_failed),
)
