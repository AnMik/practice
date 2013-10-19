from django.conf.urls import patterns
from lab3_1.views import get_content
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
    '', (r'^folders/[\w+/]+', get_content),)

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#  )
