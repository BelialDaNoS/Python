# Entrega Final CoderHouse

Este es un proyecto Django que utiliza el patrón MVT. Tiene la finalidad de poder cargar productos y clientes. Asimismo, se puede crear categorías para los productos.


Para la correcta ejecución de éste programa, será necesario contar con Python y DJango instalados.

- Python 3.x: Asegúrate de tener Python 3 instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

- Django: Asegúrate de tener Django instalado. Puedes instalarlo ejecutando el siguiente comando:
~~~python  
  pip install Django==5.0
~~~  


# Configuración de la Base de Datos ✨✍️

Desde el directorio del proyecto, ejecuta el siguiente código:
~~~bash
python manage.py migrate
~~~  

Ya estás casi listo para acceder al programa!

# Ejecución 🚀👾

Desde el directorio del proyecto, ejecuta el siguiente código:
~~~bash
python manage.py mrunserver
~~~  

Una vez hecho lo anterior, deberás visitar http://localhost:8000/myapp para poder visualizar la ejecución del programa.


**Y a cargar datos!**


# Funcionalidades ☝️🤓
Inicio (/): Muestra todas las categorías, productos y clientes.

Agregar Categoría (/add_data/categoria/): Permite agregar una nueva categoría.

Agregar Producto (/add_data/producto/): Permite agregar un nuevo producto.

Agregar Cliente (/add_data/cliente/): Permite agregar un nuevo cliente.

Buscar (/search/): Permite buscar categorías, productos y clientes en la base de datos (Por defecto, muestra todos los contenidos).


# Estructura del Proyecto 🫡🤩
myproject: Configuraciones del proyecto Django.
myapp: Aplicación principal del proyecto.
templates: Plantillas HTML.

