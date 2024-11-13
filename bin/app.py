from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Declaration du dictionnaire de donnée Combat 
# il est composer de 2 sous dictionnaire Combatant Rouge et Combatant vert avec leurs score et pénaliter
combatant = { 
    'Rouge': {'score': 0, 'cartons_blanc': 0, 'cartons_jaune': 0, 'cartons_rouge': 0, 'nom':'Combatant Rouge','Num_Licence': 0},
    'Vert': {'score': 0, 'cartons_blanc': 0, 'cartons_jaune': 0, 'cartons_rouge': 0, 'nom': 'Combatant Vert','Num_Licence': 0}
}

#Déclaration des page HTML
@app.route('/')
def index():
    return render_template('arbitrage.html')

@app.route('/affichage')
def affichage():
    return render_template('affichage.html')

@app.route('/bandeau')
def bandeau():
    return render_template('bandeau.html')
