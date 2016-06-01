"""Archivo con las url del app."""
from . views import SecretFileView
from django.conf.urls import url


urlpatterns = [
    url(
        r'^secretfile/(?P<pk>[\d]+)/$', SecretFileView.as_view(),
        name='secret_file'),
]
