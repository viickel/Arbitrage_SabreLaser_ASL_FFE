from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit  # type: ignore
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Déclaration du dictionnaire de données Combat 
# Il est composé de 2 sous-dictionnaires : 'Rouge' et 'Vert' avec leurs scores et pénalités
combatant = { 
    'Rouge': {'score': 0, 'cartons_blanc': 0, 'cartons_jaune': 0, 'cartons_rouge': 0, 'nom': 'Combatant Rouge', 'Num_Licence': 0},
    'Vert': {'score': 0, 'cartons_blanc': 0, 'cartons_jaune': 0, 'cartons_rouge': 0, 'nom': 'Combatant Vert', 'Num_Licence': 0}
}

# Déclaration des pages HTML
#@app.route('/')
#def index():
#    return render_template('arbitrage.html')

@app.route('/affichage')
def affichage():
    return render_template('affichage.html')

@app.route('/bandeau')
def bandeau():
    return render_template('bandeau.html')

@app.route('/Arene/<string:num>')
def arene(num: str):
    #return f"Arene Numero {num}"
        return render_template('arbitrage.html', num_arene = num, combatant = combatant)


if __name__ == '__main__':
    # L'application écoute sur toutes les interfaces réseau (0.0.0.0) sur le port 5000
    socketio.run(app, host='0.0.0.0', port=5000)

