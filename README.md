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
    git clone [https://github.com/tu-usuario/nombre-de-tu-repo.git](https://github.com/tu-usuario/nombre-de-tu-repo.git)
    cd nombre-de-tu-repo
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
    Crea un archivo llamado `.env` en la raíz del proyecto y añade tus credenciales y clave secreta. **¡No subas este archivo a Git!**

    ```
    SECRET_KEY=tu_clave_secreta_aleatoria_y_compleja_aqui
    DATABASE_URL=postgresql://postgres:mysecretpassword@localhost:5432/flask_db
    ```

    - Reemplaza `tu_clave_secreta_aleatoria_y_compleja_aqui` con una cadena aleatoria y muy segura (ej. `python -c "import os; print(os.urandom(24).hex())"`).
    - Asegúrate de que `DATABASE_URL` apunte a tu base de datos PostgreSQL en Docker.

5.  **Inicializa la base de datos:**
    Este paso creará las tablas `users` y `tasks` en tu base de datos PostgreSQL.

    ```bash
    python app.py
    ```

    Verás que la aplicación se inicia y luego puedes cerrarla (`Ctrl+C`). Este comando es solo para la creación inicial de las tablas.

6.  **Ejecuta la aplicación Flask:**
    ```bash
    flask run
    ```
    La aplicación debería estar disponible en `http://127.0.0.1:5000/`.

## Uso de la Aplicación

1.  **Registro:** Navega a `/register` para crear una nueva cuenta de usuario.
2.  **Inicio de Sesión:** Una vez registrado, inicia sesión en `/login` con tus credenciales.
3.  **Gestión de Tareas:** Después de iniciar sesión, podrás ver tu lista de tareas personalizada en la página principal (`/`). Puedes añadir nuevas tareas y eliminarlas.
4.  **Cierre de Sesión:** Haz clic en "Cerrar Sesión" en la barra de navegación para cerrar tu sesión.

## Contribuciones

Si alguien desea contribuir al proyecto, por favor, sigue estos pasos:

1.  Haz un "fork" del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y haz commits descriptivos.
4.  Envía tus cambios a tu "fork" (`git push origin feature/nueva-funcionalidad`).
5.  Abre un "Pull Request" a la rama `main` de este repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. (Puedes cambiar esto si lo deseas).
