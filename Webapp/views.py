from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import AdditionalInfo

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('infoPage', methods=['GET', 'POST'])
def infoPage():
    return render_template("infoPage.html")

@views.route('ApplicationPart1', methods=['GET', 'POST'])
@login_required
def ApplicationPart1():
    return render_template("applicationPart1.html", user=current_user)

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




