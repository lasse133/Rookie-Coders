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

    tasks = [
        {'title': 'First Task', 'description': 'Insert Personal Data', 'page_name' : 'Part 1', 'user_id' : current_user.id},
        {'title': 'Second Task', 'description': 'Provide Academic Ressources', 'page_name' : 'Part 1', 'user_id' : current_user.id},
        {'title': 'Third Task', 'description': 'Write Letter of Motivation', 'page_name' : 'Part 1', 'user_id' : current_user.id},
        {'title': 'Fourth Task', 'description': 'Course Selection', 'page_name' : 'Part 1', 'user_id' : current_user.id},
        {'title': 'Fifth Task', 'description': 'Send Off First Part of the Application', 'page_name' : 'Part 1', 'user_id' : current_user.id}
        ]

    for task in tasks:
            title = task['title']
            description = task['description']
            page_name = task['page_name']
            user_id = task['user_id']

             # Check if the task already exists in the database
            existing_task = Task.query.filter_by(title=title, description=description, page_name=page_name, user_id = user_id).first()

            if existing_task:
                print("Task already exists in DB.")
                # Task already exists

            else:
                new_task = Task(title=title, description=description, page_name=page_name, user_id = user_id)
                db.session.add(new_task)

    db.session.commit()

    return render_template("applicationPart1.html", user=current_user)

@views.route('/addNotePart1', methods=['POST'])
def add_notePart1():
    if request.method == 'POST':
        note = request.form.get('notePart1')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(text=note, page_name='Part 1', user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note created', category='success')
    return render_template("applicationPart1.html", user=current_user)

@views.route('/addNotePart2', methods=['POST'])
def add_notePart2():
    if request.method == 'POST':
        note = request.form.get('notePart2')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(text=note, page_name='Part 2', user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note created', category='success')
    return render_template("applicationPart2.html", user=current_user)

@views.route('/delete-note/Part1/<note_id>', methods=['POST'])
def delete_notePart1(note_id):
    note = Note.query.filter_by(id=note_id, page_name='Part 1').first()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('views.ApplicationPart1'))

@views.route('/delete-note/Part2/<note_id>', methods=['POST'])
def delete_notePart2(note_id):
    note = Note.query.filter_by(id=note_id, page_name='Part 2').first()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('views.ApplicationPart2'))

@views.route('/addTaskPart1', methods=['POST'])
def addPart1():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_task = Task(title=title, description=description, page_name='Part 1', user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added', category='success')
    return redirect(url_for('views.ApplicationPart1'))

@views.route('/addTaskPart2', methods=['POST'])
def addPart2():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_task = Task(title=title, description=description, page_name='Part 2', user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added', category='success')
    return redirect(url_for('views.ApplicationPart2'))

@views.route('/completeTaskPart1/<task_id>')
def complete_taskPart1(task_id):
    task = Task.query.filter_by(id=task_id, page_name='Part 1').first()
    task.completed = not task.completed
    db.session.commit()
    # flash('Task done', category='success')
    return redirect(url_for('views.ApplicationPart1'))

@views.route('/completeTaskPart2/<task_id>')
def complete_taskPart2(task_id):
    task = Task.query.filter_by(id=task_id, page_name='Part 2').first()
    task.completed = not task.completed
    db.session.commit()
    flash('Task done', category='success')
    return redirect(url_for('views.ApplicationPart2'))

@views.route('/deleteTaskPart1/<task_id>')
def delete_taskPart1(task_id):
    task = Task.query.filter_by(id=task_id, page_name='Part 1').first()
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted', category='success')
    return redirect(url_for('views.ApplicationPart1'))

@views.route('/deleteTaskPart2/<task_id>')
def delete_taskPart2(task_id):
    task = Task.query.filter_by(id=task_id, page_name='Part 2').first()
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted', category='success')
    return redirect(url_for('views.ApplicationPart2'))

@views.route('/save-datePart1', methods=['POST'])
def save_datePart1():
    if request.method == 'POST':
        date = request.form.get('date')
        new_date = Date(date=date, page_name='Part 1', user_id=current_user.id)
        db.session.add(new_date)
        db.session.commit()
        flash('Date saved', category='success')
        return redirect(url_for('views.ApplicationPart1'))
    
@views.route('/save-datePart2', methods=['POST'])
def save_datePart2():
    if request.method == 'POST':
        date = request.form.get('date')
        new_date = Date(date=date, page_name='Part 2', user_id=current_user.id)
        db.session.add(new_date)
        db.session.commit()
        flash('Date saved', category='success')
        return redirect(url_for('views.ApplicationPart2'))


@views.route('/displayDatePart1/<date_id>')
def displayDatePart1(date_id):
    date = Date.query.filter_by(id=date_id, page_name='Part 1').first()
    return render_template("applicationPart1.html", user=current_user, date=date)

@views.route('/displayDatePart2/<date_id>')
def displayDatePart2(date_id):
    date = Date.query.filter_by(id=date_id, page_name='Part 2').first()
    return render_template("applicationPart2.html", user=current_user, date=date)

@views.route('/deleteDatePart1/<date_id>')
def delete_datePart1(date_id):
    date = Date.query.filter_by(id=date_id, page_name='Part 1').first()
    db.session.delete(date)
    db.session.commit()
    flash('Date deleted', category='success')
    return redirect(url_for('views.ApplicationPart1'))

@views.route('/deleteDatePart2/<date_id>')
def delete_datePart2(date_id):
    date = Date.query.filter_by(id=date_id, page_name='Part 2').first()
    db.session.delete(date)
    db.session.commit()
    flash('Date deleted', category='success')
    return redirect(url_for('views.ApplicationPart2'))



@views.route('ApplicationPart2', methods=['GET', 'POST'])
@login_required
def ApplicationPart2():
    
    tasks = [
        {'title': 'Sixth Task', 'description': 'Insert Personal Data Part Two', 'page_name' : 'Part 2', 'user_id' : current_user.id},
        {'title': 'Seventh Task', 'description': 'Provide Fincancial Sources', 'page_name' : 'Part 2', 'user_id' : current_user.id},
        {'title': 'Eighth Task', 'description': 'Send off Second Part of the Application', 'page_name' : 'Part 2', 'user_id' : current_user.id},
        {'title': 'Ninth Task', 'description': 'Arrange Appointment with Consulate', 'page_name' : 'Part 2', 'user_id' : current_user.id},
        {'title': 'Tenth Task', 'description': 'Conclude Foreign Insurance', 'page_name' : 'Part 2', 'user_id' : current_user.id},
        {'title': 'Eleventh Task', 'description': 'Find Housing', 'page_name' : 'Part 2', 'user_id' : current_user.id}
        ]

    for task in tasks:
            title = task['title']
            description = task['description']
            page_name = task['page_name']
            user_id = task['user_id']

             # Check if the task already exists in the database
            existing_task = Task.query.filter_by(title=title, description=description, page_name=page_name, user_id = user_id).first()

            if existing_task:
                print("Task already exists in DB.")
                # Task already exists

            else:
                new_task = Task(title=title, description=description, page_name=page_name, user_id = user_id)
                db.session.add(new_task)

    db.session.commit()
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




