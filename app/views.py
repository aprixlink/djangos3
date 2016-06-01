"""Archivo que contiene las vistas del app."""

from boto.s3.connection import S3Connection
from django import http
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from . models import File
from djangos3.settings import AWS_ACCESS_KEY_ID
from djangos3.settings import AWS_SECRET_ACCESS_KEY
from djangos3.settings import AWS_STORAGE_BUCKET_NAME
from djangos3.settings import MEDIA_DIRECTORY
import logging
logger = logging.getLogger('django.request')


class SecretFileView(RedirectView):
    """Vista que permite ver los archivos privados."""

    def get_redirect_url(self, **kwargs):
        """Retorna una url que dura 60 segundos."""
        s3 = S3Connection(
            AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, is_secure=True)
        # Crea una url valida por 60 segundos.
        return s3.generate_url(
            60, 'GET', bucket=AWS_STORAGE_BUCKET_NAME, key=kwargs['filepath'],
            force_http=True)

    def get(self, request, *args, **kwargs):
        m = get_object_or_404(File, pk=kwargs['pk'])
        u = request.user

        # Verifica si es un usuario autenticado o si hace parte del staff.
        if u.is_authenticated() and u.is_staff:
            if m.private_file:
                filepath = MEDIA_DIRECTORY + str(m.private_file)
                url = self.get_redirect_url(filepath=filepath)
                # Redirige y devuelve el codigo Http correspondiente.
                if url:
                    return http.HttpResponseRedirect(url)
                else:
                    logger.warning(
                        'Gone: %s', self.request.path,
                        extra={
                            'status_code': 410,
                            'request': self.request
                            })
                    return http.HttpResponseGone()
            else:
                raise http.Http404
        else:
            raise http.Http404
