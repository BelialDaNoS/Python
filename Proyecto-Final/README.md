# Mi Proyecto Django

Este es un proyecto Django que utiliza el patrón MVT y tiene las siguientes características:

1. **Configuración del entorno:**
   - Asegúrate de tener Python y Django instalados en tu sistema.
   - Instala Django con `pip install django`.
   - Crea un nuevo proyecto y una nueva aplicación.

2. **Definición de modelos:**
   - Editar `myapp/models.py` para incluir al menos tres clases: `Categoria`, `Producto`, y `Cliente`.
   - Realiza migraciones y aplica los cambios en la base de datos.

3. **Creación de formularios:**
   - Crea un archivo `myapp/forms.py` para definir formularios para cada clase de modelo.

4. **Creación de vistas y plantillas:**
   - Editar `myapp/views.py` para incluir vistas para la página principal, agregar datos y buscar en la base de datos.
   - Crea las plantillas HTML en el directorio `templates`.

5. **Configuración de URLs:**
   - Editar `myapp/urls.py` para incluir las rutas a las vistas.

6. **Configuración de plantillas base:**
   - Crear un archivo `base.html` en el directorio `templates` para manejar la herencia HTML.

7. **Creación de README:**
   - Documenta el orden en el que se prueban las cosas.
   - Proporciona información sobre las funcionalidades y cómo ejecutar la aplicación.

8. **Ejecución del proyecto:**
   - Ejecuta `python manage.py runserver` para iniciar el servidor de desarrollo.
   - Visita [http://localhost:8000/](http://localhost:8000/) en tu navegador para ver la aplicación.

¡Disfruta desarrollando tu proyecto Django!
