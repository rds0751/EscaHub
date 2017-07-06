from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url

from EscaHub.authentication import views as EscaHub_auth_views
from EscaHub.core import views as core_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', core_views.home, name='home'),
    url(r'^signup/$', EscaHub_auth_views.signup, name='signup'),
    url(r'^login/', auth_views.login, {'template_name': 'authentication/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name': 'authentication/logout.html'}, name='logout'),
    url(r'^blog/', include('EscaHub.blog.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^messages/', include('EscaHub.messenger.urls')),
    # url(r'^EscaHub/', include('EscaHub.EscaHub.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls, ),
]
