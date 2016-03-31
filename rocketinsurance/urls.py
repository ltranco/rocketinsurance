from django.conf.urls import include, url
from django.contrib import admin

from insuranceintro import views as insuranceintro_views
urlpatterns = [
    # Examples:
    # url(r'^$', 'rocketinsurance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^element/', insuranceintro_views.ElementView.as_view()),
    url(r'^termq/', insuranceintro_views.TermView.as_view()),
    url(r'^permq/', insuranceintro_views.PermView.as_view()),
    url(r'^contact/', insuranceintro_views.ContactView.as_view()),
    url(r'^$', insuranceintro_views.IndexView.as_view()),
]
