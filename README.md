## TO-DO App con Flask y PostgreSQL

## Características

- **Autenticación de Usuarios:** Registro, inicio de sesión y cierre de sesión.
- **Gestión de Tareas:** Los usuarios pueden agregar y eliminar tareas.
- **Persistencia de Datos:** Utiliza PostgreSQL para almacenar usuarios y tareas.
- **Seguridad:** Hashing de contraseñas con Werkzeug y uso de sesiones seguras.
- **Modularidad:** Estructura de proyecto organizada con Blueprints y módulos de modelos.
- **Base de Datos Relacional:** Implementación de relaciones "uno a muchos" entre usuarios y tareas.
- **Diseño Básico:** Uso de Bootstrap para una interfaz de usuario simple y responsiva.

## Tecnologías Utilizadas

- **Python 3.x**
- **Flask:** Microframework web.
- **Flask-SQLAlchemy:** Extensión para integrar SQLAlchemy (ORM) con Flask.
- **SQLAlchemy:** ORM (Object Relational Mapper) para interacción con la base de datos.
- **Psycopg2:** Adaptador de PostgreSQL para Python.
- **Werkzeug:** Utilidades para hashing de contraseñas.
- **python-dotenv:** Para cargar variables de entorno desde un archivo `.env`.
- **PostgreSQL:** Sistema de gestión de bases de datos relacionales (ejecutado vía Docker).
- **Bootstrap 5:** Framework CSS para estilos.

## Requisitos del Sistema

Antes de iniciar la aplicación, asegúrate de tener instalado:

- **Python 3.8+**
- **pip** (gestor de paquetes de Python)

## Configuración e Inicio de la Aplicación

1.  **Clona el repositorio:**

    ```bash
    git clone [https://github.com/martintribuzio/istea-programacion1-todo](https://github.com/martintribuzio/istea-programacion1-todo)
    cd istea-programacion1-todo
    ```

2.  **Crea y activa un entorno virtual:**

    ```bash
    python -m venv venv
    # En Windows: .\venv\Scripts\activate
    # En macOS/Linux: source venv/bin/activate
    ```

3.  **Instala las dependencias de Python:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Crea el archivo de variables de entorno:**
    Crea un archivo llamado `.env` en la raíz del proyecto a partir del archivo `.env.example` y configura las variables necesarias:

    ```bash
    cp .env.example .env
    ```

5.  **Inicializa la base de datos:**
    Este paso creará las tablas `users` y `tasks` en tu base de datos PostgreSQL.

    ```bash
    python app.py
    ```

## Uso de la Aplicación

1.  **Registro:** Navega a `/register` para crear una nueva cuenta de usuario.
2.  **Inicio de Sesión:** Una vez registrado, inicia sesión en `/login` con tus credenciales.
3.  **Gestión de Tareas:** Después de iniciar sesión, podrás ver tu lista de tareas personalizada en la página principal (`/`). Puedes añadir nuevas tareas y eliminarlas.
4.  **Cierre de Sesión:** Haz clic en "Cerrar Sesión" en la barra de navegación para cerrar tu sesión.
