from extensions import db # Importamos la instancia de db

class Task(db.Model):
    __tablename__ = 'tasks' # Nombre de la tabla en la DB

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    # 'user.id' se refiere al nombre de la tabla ('user') y su columna 'id'.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.content}>'