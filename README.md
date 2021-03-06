## Primera aplicación web con Flask y Python

Introducción al desarrollo de páginas y aplicaciones web usando el lenguaje de programación Python y uno de los frameworks web más usados y demandados actualmente: Flask.

### Paquetes instalados en el entorno virtual
Manejador de la aplicación y el servidor del entorno virtual
```
pip install flask-script
```
Protección CSRF (Cross-site Request Forgery): Solicitud de falsificación entre sitios.
```
pip install Flask-WTF
```
Contectividad con base de datos MySQL
```
pip install mysqlclient flask-mysql flask-mysqldb
```
Encriptación de contraseñas
```
from werkzeug.security import generate_password_hash, check_password_hash
```
Manejo de sesiones
```
pip install flask-login
```

### Iniciar entorno virtual
```
python manage.py runserver
```

### Convertir modelos en un paquete de Python
Crear el archivo `__init__.py` en la carpeta

### Liga de recursos del curso
[Codigofacilito](https://github.com/codigofacilito/primera-app-flask)