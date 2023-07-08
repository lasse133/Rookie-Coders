from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from .models import Note, Date, Task
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('infoPage', methods=['GET', 'POST'])
def infoPage():
    return render_template("infoPage.html")

@views.route('ApplicationPart1', methods=['GET', 'POST', 'DELETE'])
@login_required
def ApplicationPart1():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(text=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note created', category='success')
        
    return render_template("applicationPart1.html", user=current_user)


@views.route('/delete-note/<note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('views.ApplicationPart1'))

@views.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_task = Task(title=title, description=description, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added', category='success')
    return redirect(url_for('views.ApplicationPart1'))

@views.route('/complete/<task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash('Task done', category='success')
    return redirect(url_for('views.ApplicationPart1'))

@views.route('/delete/<task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted', category='success')
    return redirect(url_for('views.ApplicationPart1'))

@views.route('ApplicationPart2', methods=['GET', 'POST'])
@login_required
def ApplicationPart2():
    return render_template("applicationPart2.html", user=current_user)

@views.route('SubTaskPersonalData', methods=['GET', 'POST'])
def SubTaskPersonalData():
    return render_template("subTaskPersonal.html", user=current_user)

@views.route('SubTaskAcademicRessources', methods=['GET', 'POST'])
def SubTaskAcademicRessources():
    return render_template("subTaskAcademic.html", user=current_user)

@views.route('SubTaskFinancialRessources', methods=['GET', 'POST'])
def SubTaskFinancialRessources():
    return render_template("subTaskFinancial.html", user=current_user)




