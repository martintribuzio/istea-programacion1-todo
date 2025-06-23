from extensions import db # Importamos la instancia de db

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users' # Nombre de la tabla

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False) # Para almacenar el hash de la contraseña

    # Relación uno a muchos: Un usuario puede tener muchas tareas

    # 'Task' = nombre de la clase del modelo Task.
    # 'backref='user'' crea una propiedad 'user' en el objeto Task.
    # 'lazy=True' significa que las tareas relacionadas se cargan solo cuando se acceden.
    tasks = db.relationship('Task', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    # Métodos para manejar contraseñas de forma segura
    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password_hash, password)