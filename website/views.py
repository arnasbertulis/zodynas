from flask import Blueprint, render_template, request, session
from .zodziai_reiksmes import zodynas
import random

views = Blueprint('views', __name__)

@views.route("/", methods=['POST', 'GET'])
def home():
  if request.method == 'GET':
    session['score'] = 0
    session['attempts'] = 0
    session['guesses'] = 0

    session['zodziai'] = []
    session['reiksmes'] = []
    session['teisingas_atsakymas'] = 0

  if request.method == 'POST':
    if request.form['choice'] == session['reiksmes'][session['teisingas_atsakymas']]:
      session['score'] += 1
      session['guesses'] += 1
    else:
      session['score'] = 0
    session['attempts'] += 1

  session['reiksmes'] = []
  session['zodziai'] = []
  session['teisingas_atsakymas'] = random.randint(0, 3)
  for _ in range(4):
    zodis, reiksme = random.choice(list(zodynas.items()))
    session['zodziai'].append(zodis)
    session['reiksmes'].append(reiksme)
  
  return render_template('quiz.html', zodis=session['zodziai'][session['teisingas_atsakymas']].lower(), reiksmes=session['reiksmes'], teisingas_atsakymas=session['teisingas_atsakymas'], score=session['score'], attempts=session['attempts'], guesses=session['guesses'])