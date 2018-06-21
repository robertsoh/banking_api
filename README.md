- Activar el entorno virtual
- Configuración de variables de entorno para el sistema:
```
    SECRET_KEY=secret_key
    DJANGO_SETTINGS_MODULE=config.settings.dev
    ALLOWED_HOSTS=localhost
    DB_NAME=db_name
    DB_USER=db_user
    DB_HOST=db_host
    DB_PORT=db_port
```
- Ejecutar las migraciones: `python manage.py migrate`
- Crear usuario administrador: `python manage.py createsuperuser`
- Ejecutar el servidor: `python manage.py runserver`

---
QOILABS © 2018
