from django.conf.urls import include, url
from django.contrib import admin

from insuranceintro import views as insuranceintro_views
urlpatterns = [
    # Examples:
    # url(r'^$', 'rocketinsurance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^element/', insuranceintro_views.ElementView.as_view()),
    url(r'^q/', insuranceintro_views.QuestionView.as_view()),
    url(r'^$', insuranceintro_views.IndexView.as_view()),
]
