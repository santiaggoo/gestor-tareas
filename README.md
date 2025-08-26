Aplicación web desarrollada con Django para gestionar tareas personales.
Permite a los usuarios registrarse, iniciar sesión, crear, editar y eliminar tareas
Funcionalidades

- Registro y autenticación de usuarios
- Creación de tareas con título y descripción
- Edición y eliminación de tareas
- Vista de lista de tareas por usuario

Tecnologías usadas

-Python
-Django
-HTML y CSS

 Instalación del proyecto
1. Clonar el repositorio
git clone https://github.com/santiaggoo/gestor-tareas.git

2. Crear y activar un entorno virtual
python -m venv env
source env/bin/activate  # En Linux/macOS
env\Scripts\activate     # En Windows

3. Instalar dependencias
pip install -r requirements.txt

4. Configurar la base de datos
python manage.py migrate

6. Ejecutar el servidor
python manage.py runserver


Luego abre tu navegador y accede a:
 http://127.0.0.1:8000/register para registrar un usuario 
 http://127.0.0.1:8000/login    para inicar sesion con el usuario ya creado
