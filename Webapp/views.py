from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from .models import Note, Date, Task
from . import db

# For the basics: Notebook from class: https://hwrberlin.github.io/fswd/ (Full Stack Web Dev @ HWR Berlin)

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('infoPage', methods=['GET', 'POST'])
def infoPage():
    return render_template("infoPage.html")

# Hilfe von OpenAI (2023)
def addTask(title, description, page_name, user_id):
             # Check if the task already exists in the database
            existing_task = Task.query.filter_by(title=title, description=description, page_name=page_name, user_id = user_id).first()

            if existing_task:
                print("Task already exists in DB.")
                # Task already exists

            else:
                new_task = Task(title=title, description=description, page_name=page_name, user_id = user_id)
                db.session.add(new_task)
                db.session.commit()

@views.route('ApplicationPart1', methods=['GET', 'POST', 'DELETE'])
@login_required
def ApplicationPart1():

    tasks = [
        {'title': 'First Task', 'description': 'Insert Personal Data (See Documents for Details)', 'page_name' : 'Part1', 'user_id' : current_user.id},
        {'title': 'Second Task', 'description': 'Provide Academic Ressources (See Documents for Details)', 'page_name' : 'Part1', 'user_id' : current_user.id},
        {'title': 'Third Task', 'description': 'Write Letter of Motivation', 'page_name' : 'Part1', 'user_id' : current_user.id},
        {'title': 'Fourth Task', 'description': 'Course Selection', 'page_name' : 'Part1', 'user_id' : current_user.id},
        {'title': 'Fifth Task', 'description': 'Send Off First Part of the Application', 'page_name' : 'Part1', 'user_id' : current_user.id}
        ]
    for task in tasks:
            addTask(task['title'], task['description'], task['page_name'], task['user_id'])
    return render_template("applicationPart1.html", user=current_user)


@views.route('ApplicationPart2', methods=['GET', 'POST'])
@login_required
def ApplicationPart2():
    
    tasks = [
        {'title': 'Sixth Task', 'description': 'Insert Personal Data Part Two (See Documents for Details)', 'page_name' : 'Part2', 'user_id' : current_user.id},
        {'title': 'Seventh Task', 'description': 'Provide Financial Sources', 'page_name' : 'Part2', 'user_id' : current_user.id},
        {'title': 'Eighth Task', 'description': 'Send off Second Part of the Application', 'page_name' : 'Part2', 'user_id' : current_user.id},
        {'title': 'Ninth Task', 'description': 'Arrange Appointment with Consulate', 'page_name' : 'Part2', 'user_id' : current_user.id},
        {'title': 'Tenth Task', 'description': 'Conclude Foreign Insurance', 'page_name' : 'Part2', 'user_id' : current_user.id},
        {'title': 'Eleventh Task', 'description': 'Find Housing', 'page_name' : 'Part2', 'user_id' : current_user.id}
        ]
    for task in tasks:
        addTask(task['title'], task['description'], task['page_name'], task['user_id'])
    return render_template("applicationPart2.html", user=current_user)

@views.route('SubTaskPersonalData', methods=['GET', 'POST'])
def SubTaskPersonalData():
    tasks = [
        {'title': 'First Document', 'description': 'Copy of Passport', 'page_name' : 'PersonalData', 'user_id' : current_user.id},
        {'title': 'Second Document', 'description': 'Covid-19 Vaccination Certificate', 'page_name' : 'PersonalData', 'user_id' : current_user.id},
        {'title': 'Third Document', 'description': 'Vaccination Certificate', 'page_name' : 'PersonalData', 'user_id' : current_user.id},
        ]

    for task in tasks:
        addTask(task['title'], task['description'], task['page_name'], task['user_id'])
    return render_template("subTaskPersonal.html", user=current_user)

@views.route('SubTaskAcademicRessources', methods=['GET', 'POST'])
def SubTaskAcademicRessources():
    tasks = [
        {'title': 'First Document', 'description': 'Transcripts', 'page_name' : 'AcademicRessources', 'user_id' : current_user.id},
        {'title': 'Second Document', 'description': 'Performance Overview', 'page_name' : 'AcademicRessources', 'user_id' : current_user.id},
        ]
    for task in tasks:
        addTask(task['title'], task['description'], task['page_name'], task['user_id'])
    return render_template("subTaskAcademic.html", user=current_user)

@views.route('SubTaskFinancialRessources', methods=['GET', 'POST'])
def SubTaskFinancialRessources():
    tasks = [
        {'title': 'First Document', 'description': 'Proof of Funding', 'page_name' : 'FinancialRessources', 'user_id' : current_user.id},
        {'title': 'Second Document', 'description': 'Proof of Scholarship', 'page_name' : 'FinancialRessources', 'user_id' : current_user.id},
        ]
    for task in tasks:
        addTask(task['title'], task['description'], task['page_name'], task['user_id'])
    return render_template("subTaskFinancial.html", user=current_user)


# TechWithTim (2023, 29. Januar)
@views.route('/addNote/<page_name>', methods=['POST'])
def add_note(page_name):
    note = request.form.get('note' + page_name)
    if len(note) < 1:
        flash('Note is too short', category='error')
    else:
        new_note = Note(text=note, page_name=page_name, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note created', category='success')
    return redirect(url_for("views.Application" + page_name, page_name=page_name, user=current_user))


# TechWithTim (2023, 29. Januar)
@views.route('/deleteNote/<page_name>/<note_id>', methods=['POST'])
def delete_note(page_name,note_id):
    note = Note.query.filter_by(id=note_id, page_name= page_name).first()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("views.Application" + page_name, page_name=page_name, user=current_user))

# patrickloeber (2020, 13. Dezember)
@views.route('/addPersonalTask/<page_name>', methods=['POST'])
def addPersonalTask(page_name):
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_task = Task(title=title, description=description, page_name=page_name, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added', category='success')
    return redirect(url_for('views.Application' + page_name, page_name=page_name))

# patrickloeber (2020, 13. Dezember)
@views.route('/addPersonalSubTask/<page_name>', methods=['POST'])
def addPersonalSubTask(page_name):
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_task = Task(title=title, description=description, page_name=page_name, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added', category='success')
    return redirect(url_for('views.SubTask' + page_name, page_name=page_name))

# completion routes  with help from OpenAI (2023)
@views.route('/completeTask/<page_name>/<task_id>')
def complete_task(page_name,task_id):
    task = Task.query.filter_by(id=task_id, page_name= page_name).first()
    task.completed = not task.completed
    db.session.commit()
    # flash('Task done', category='success')
    return redirect(url_for('views.Application' + page_name, page_name=page_name))

# completion routes  with help from OpenAI (2023)
@views.route('/completeSubTask/<page_name>/<task_id>')
def complete_subTask(page_name,task_id):
    task = Task.query.filter_by(id=task_id, page_name= page_name).first()
    task.completed = not task.completed
    db.session.commit()
    # flash('Task done', category='success')
    return redirect(url_for('views.SubTask' + page_name, page_name=page_name))


# patrickloeber (2020, 13. Dezember)
@views.route('/deleteTask/<page_name>/<task_id>')
def delete_task(page_name,task_id):
    task = Task.query.filter_by(id=task_id, page_name=page_name).first()
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted', category='success')
    return redirect(url_for('views.Application' + page_name, page_name=page_name))

# patrickloeber (2020, 13. Dezember)
@views.route('/deleteSubTask/<page_name>/<task_id>')
def delete_subTask(page_name,task_id):
    task = Task.query.filter_by(id=task_id, page_name=page_name).first()
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted', category='success')
    return redirect(url_for('views.SubTask' + page_name, page_name=page_name))

# Saving routes: Hilfe von OpenAI (2023)
@views.route('/saveDate/<page_name>', methods=['POST'])
def save_date(page_name):
    if request.method == 'POST':
        existing_date = Date.query.filter_by(page_name=page_name, user_id=current_user.id).first()

        if existing_date:
            flash('You have already added a date. Please delete your existing date before adding a new one.', category='error')
        else:
            date = request.form.get('date')
            if date.strip():    
                new_date = Date(date=date, page_name=page_name, user_id=current_user.id)
                db.session.add(new_date)
                db.session.commit()
                flash('Date saved', category='success')
            else:
                flash('Enter a date', category='error')
    return redirect(url_for('views.Application' + page_name, page_name=page_name))

@views.route('/deleteDate/<page_name>/<date_id>')
def delete_date(page_name,date_id):
    date = Date.query.filter_by(id=date_id, page_name=page_name).first()
    db.session.delete(date)
    db.session.commit()
    flash('Date deleted', category='success')
    return redirect(url_for('views.Application' + page_name))
