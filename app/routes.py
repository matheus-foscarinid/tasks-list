from flask import Blueprint, render_template, request, redirect
from .models import Task, db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@tasks_bp.route('/sobre')
def about():
    return "Olá, este é um aplicativo de lista de tarefas!"

@tasks_bp.route('/add', methods=['POST'])
def nova_tarefa():
    description = request.form['task']
    if description:
        new_task = Task(description=description, done=False)
        db.session.add(new_task)
        db.session.commit()
    return redirect('/')

@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.done = not task.done
        db.session.commit()
    return redirect('/')

@tasks_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect('/')
    if request.method == 'POST':
        new_desc = request.form['description']
        if new_desc:
            task.description = new_desc
            db.session.commit()
        return redirect('/')
    return render_template('edit.html', task=task)

