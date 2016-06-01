"""Archivo que contiene herramientras utiles para el S3."""
from storages.backends.s3boto import S3BotoStorage

# Define el servicio para la carpeta static en S3.
StaticS3BotoStorage = lambda: S3BotoStorage(location='static')
# Define el servicio para la carpeta media en S3.
MediaS3BotoStorage = lambda: S3BotoStorage(location='media')
