from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from extensions import db # Importamos la instancia de db
from models.user import User

# Creamos un blueprint para las rutas
authBP = Blueprint('auth', __name__)

@authBP.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validacion de datos
        if not username or not password:
            flash('Completa todos los campos.', 'error')
            return redirect(url_for('auth.register'))

        # Verificamos si existe el user
        existingUser = User.query.filter_by(username=username).first()

        if existingUser:
            flash('Nombre de usuario en uso', 'error')
            return redirect(url_for('auth.register'))

        # Crear nuevo usuario
        newUser = User(username=username)
        newUser.setPassword(password)

        # Guardar el nuevo user
        db.session.add(newUser)
        db.session.commit()

        flash('Registro exitoso!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@authBP.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        # Verificar credenciales
        if user and user.checkPassword(password):
            session['user_id'] = user.id

            flash('Inicio de sesion exitoso', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')


@authBP.route('/logout')
def logout():
    session.pop('user_id', None)

    flash('Cierre de sesion exitoso', 'info')
    return redirect(url_for('main.home'))