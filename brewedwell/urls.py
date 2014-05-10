from django.conf.urls import patterns, include, url
from engine.views import HomeView, BreweryListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brewedwell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^breweries/$', BreweryListView.as_view(), name='brewery-list'),
)
