from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> HI </h1>"

@views.infoPage('infoPage')
def infoPage():
    return "<h1> InfoPage </h1>"

@views.infoPage('ApplicationPart1')
def ApplicationPart1():
    return "<h1> ApplicationPart1 </h1>"

@views.infoPage('ApplicationPart2')
def ApplicationPart2():
    return "<h1> ApplicationPart2 </h1>"

@views.infoPage('SubTaskPersonalData')
def SubTaskPersonalData():
    return "<h1> SubTaskPersonalData </h1>"

@views.infoPage('SubTaskAcademicRessources')
def SubTaskAcademicRessources():
    return "<h1> SubTaskAcademicRessources </h1>"

@views.infoPage('SubTaskFinancialRessources')
def SubTaskFinancialRessources():
    return "<h1> SubTaskFinancialRessources </h1>"

@views.infoPage('SubTaskForeignInsurance')
def SubTaskForeignInsurance():
    return "<h1> SubTaskForeignInsurance </h1>"



