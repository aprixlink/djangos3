Instrucciones de uso.

**IAM**

1) Se crea un usuario en:
https://console.aws.amazon.com/iam/home#users

2) Se hace clic en el usuario creado -> Permissions -> Attach Policy y se agrega el permiso `AmazonS3FullAccess`.

**S3**

1) Se crea el bucket en https://console.aws.amazon.com/s3/home

2) Se hace clic en el bucket y luego se da clic en Properties -> Permissions -> Edit bucket policy.

3) Se agrega la siguiente política:

    {
    	"Version": "2008-10-17",
    	"Id": "Archivos publicos - privados.",
    	"Statement": [
    		{
    			"Sid": "Allow Signed Downloads for Private Files",
    			"Effect": "Allow",
    			"Principal": {
    				"AWS": "<<USUARIO-arn>>"
    			},
    			"Action": "s3:GetObject",
    			"Resource": "arn:aws:s3:::<<NOMBRE-DEL-BUCKET>>-app/media/private/*"
    		},
    		{
    			"Sid": "Allow Static Files",
    			"Effect": "Allow",
    			"Principal": {
    				"AWS": "<<USUARIO-arn>>"
    			},
    			"Action": "s3:GetObject",
    			"Resource": "arn:aws:s3:::<<NOMBRE-DEL-BUCKET>>/static/*"
    		}
    	]
    }

4) Cambiar `<<USUARIO-arn>>` por el arn del usuario creado en IAM.

5) Cambiar `<<NOMBRE-DEL-BUCKET>>` por el nombre del bucket creado en S3.

**Django**

1) Asignar los valores correspondientes en el archivo djangos3/settings.py:

    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME

2) Hacer migrate a la base de datos: `python manage.py migrate`

3) Crear un superusuario: `python manage.py createsuperuser`

4) Ejecutar el servidor web: `python manage.py runserver`

5) Entrar a http://127.0.0.1:8000/admin/app/file/

6) Subir dos archivos uno publico y otro privado para cada objeto Archivo.

7) Para hacer la prueba de la url que solo dura 60 segundos se debe ir a la siguiente url: http://127.0.0.1:8000/secretfile/X/ donde `X` es el id del objeto Archivo en la base de datos.

8) Comprobar que la url solo dura 60 segundos.
