from flask import Flask, render_template
from extensions import db
from config import Config

# 1 ---- Inicializacion de la app ---- #
app = Flask(__name__)

# 2 ---- Carga de configuracion ---- #
app.config.from_object(Config)

# 3 ---- Inicializacion de la base de datos ---- #
db.init_app(app)

# 4 ---- Registro de rutas ---- #
from routes.auth import authBP
from routes.main import mainBP

app.register_blueprint(authBP)
app.register_blueprint(mainBP)

# 5 ---- Manejo de errores ---- #
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        # Creamos las tablas de la db si no existen
        db.create_all() 

    # Inicia el servidor de desarrollo
    app.run(debug=True)