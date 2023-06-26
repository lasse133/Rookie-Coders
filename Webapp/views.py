from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('infoPage')
def infoPage():
    return render_template("infoPage.html")

@views.route('ApplicationPart1')
@login_required
def ApplicationPart1():
    return render_template("applicationPartX.html", user=current_user)

@views.route('ApplicationPart2')
@login_required
def ApplicationPart2():
    return render_template("applicationPartX.html", user=current_user)

@views.route('SubTaskPersonalData')
def SubTaskPersonalData():
    return render_template("applicationPartX.html", user=current_user)

@views.route('SubTaskAcademicRessources')
def SubTaskAcademicRessources():
    return render_template("applicationPartX.html", user=current_user)

@views.route('SubTaskFinancialRessources')
def SubTaskFinancialRessources():
    return render_template("applicationPartX.html", user=current_user)




