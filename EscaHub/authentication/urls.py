from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url

from EscaHub.authentication import views as EscaHub_auth_views

urlpatterns = [
    url(r'^logout/$', 'EscaHub_auth_views.logout_view', name='auth_logout'),
    url(r'^login/$', 'EscaHub_auth_views.login_view', name='auth_login'),
    url(r'^register/$', 'EscaHub_auth_views.registration_view', name='auth_register'),
    url(r'^address/add/$', 'EscaHub_auth_views.add_user_address', name='add_user_address'),
    url(r'^activate/(?P<activation_key>\w+)/$', 'EscaHub_auth_views.activation_view', name='activation_view'),
]