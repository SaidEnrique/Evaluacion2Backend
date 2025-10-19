import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluacion2.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'ES02'
password = 'pbe-es-02'
email = 'es02@example.com'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser creado: ES02')
else:
    print('El usuario ES02 ya existe')
