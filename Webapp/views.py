from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import AdditionalInfo
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
        new_note = AdditionalInfo(text=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()

    if request.method == 'DELETE':
        db.session.delete(db.session.get(AdditionalInfo.id))
        del AdditionalInfo.text
        db.session.commit()
    
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

#@views.route('/delete-note', methods=['POST'])
#def delete_note():
 #   note = json.loads(request.data)
  #  noteId = note['noteId']
   # note = AdditionalInfo.query.get(noteId)
    #if note:
     #   if note.user_id == current_user.id:
      #      db.session.delete(note)
       #     db.session.commit()
    
    
    #return jsonify({})



