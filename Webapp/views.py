from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('infoPage')
def infoPage():
    return render_template("infoPage.html")

@views.route('ApplicationPart1')
def ApplicationPart1():
    return render_template("applicationPartX.html")

@views.route('ApplicationPart2')
def ApplicationPart2():
    return render_template("applicationPartX.html")

@views.route('SubTaskPersonalData')
def SubTaskPersonalData():
    return render_template("applicationPartX.html")

@views.route('SubTaskAcademicRessources')
def SubTaskAcademicRessources():
    return render_template("applicationPartX.html")

@views.route('SubTaskFinancialRessources')
def SubTaskFinancialRessources():
    return render_template("applicationPartX.html")

@views.route('SubTaskForeignInsurance')
def SubTaskForeignInsurance():
    return render_template("applicationPartX.html")



