"""Archivo que contiene los modelos de mi app."""
from django.db import models
from django.utils.encoding import smart_text


class S3PrivateFileField(models.FileField):

    def __init__(
        self, verbose_name=None, name=None, upload_to='', storage=None,
            **kwargs):

        super(S3PrivateFileField, self).__init__(
            verbose_name=verbose_name, name=name, upload_to=upload_to,
            storage=storage, **kwargs)
        self.storage.default_acl = "private"


class File(models.Model):
    """Modelo para subir imagenes."""

    name = models.CharField('Nombre', max_length=100)
    public_file = models.FileField(
        'Archivo publico', blank=True, null=True, upload_to='public/')
    private_file = S3PrivateFileField(
        'Archivo privado', blank=True, null=True, upload_to='private/')

    class Meta(object):
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

    def __str__(self):
        return smart_text(self.name)
