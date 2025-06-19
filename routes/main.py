from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from extensions import db
from models.task import Task
from models.user import User

mainBP = Blueprint('main', __name__)

@mainBP.route('/')
def home():
    user = None
    tasks = []

    if 'user_id' in session:
        userId = session['user_id']
        currentUser = User.query.get(userId)

        if currentUser:
            tasks = user.tasks
        else:
            session.pop('user_id', None)
            flash('Inicia sesion', 'error')

    return render_template('home.html', tasks=tasks, user=user)


@mainBP.route('/task', methods=['POST'])
def createTask():
    if 'user_id' not in session:
        flash('Debes iniciar sesion para añadir tareas', 'error')
        return redirect(url_for('auth.login'))

    newTask = request.form.get('task')
    userId = session['user_id']

    if newTask:
        task = Task(content=newTask, user_id=userId)
        db.session.add(task)
        db.session.commit()
        flash('Tarea agregada exitosamente', 'success')
    else:
        flash('El nombre de la tarea es requerido', 'error')

    return redirect(url_for('main.home'))


@mainBP.route('/task/delete/<int:taskId>', methods=['POST'])
def delete_task(taskId):
    if 'user_id' not in session:
        flash('Tenes que iniciar sesion para eliminar tareas', 'error')
        return redirect(url_for('auth.login'))

    userId = session['user_id']
    taskToDelte = Task.query.filter_by(id=taskId, user_id=userId).first()

    if taskToDelte:
        db.session.delete(taskToDelte)
        db.session.commit()
        flash('Tarea eliminada', 'success')
    else:
        flash('No se pudo eliminar la tarea', 'error')
    
    return redirect(url_for('main.home'))