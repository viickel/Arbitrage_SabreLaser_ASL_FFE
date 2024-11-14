from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit  # type: ignore
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Déclaration du dictionnaire de données Combat 
# Il est composé de 2 sous-dictionnaires : 'Rouge' et 'Vert' avec leurs scores et pénalités
combatant = { 
    'Rouge': {'score': 0, 'cartons_blanc': 0, 'cartons_jaune': 0, 'cartons_rouge': 0, 'nom': 'Combatant Rouge', 'Num_Licence': 0,'Quest':0},
    'Vert': {'score': 0, 'cartons_blanc': 0, 'cartons_jaune': 0, 'cartons_rouge': 0, 'nom': 'Combatant Vert', 'Num_Licence': 0,'Quest':0}
}

# Dictionnaire pour stocker les données de chaque arène
combatant_arene = {}

# Fonction d'initialisation pour créer une arène si elle n'existe pas déjà
def init_combatant_arene(num):
     if num not in combatant_arene:
          # Clone le modèle de combatant pour l'arène donnée
          combatant_arene[num] = {
               'Rouge': combatant['Rouge'].copy(),
               'Vert' : combatant['Vert'].copy()
          }

@app.route('/affichage/<string:num>')
def affichage(num: str):
    init_combatant_arene(num)
    return render_template('affichage.html', num_arene=num, combatant=combatant_arene[num])

@app.route('/bandeau/<string:num>')
def bandeau(num: str):
    init_combatant_arene(num)
    return render_template('bandeau.html', num_arene=num, combatant=combatant_arene[num])

@app.route('/Arene/<string:num>')
def arene(num: str):
    init_combatant_arene(num)
    return render_template('arbitrage.html', num_arene=num, combatant=combatant_arene[num])


@socketio.on('maj_score')
def handle_maj_score(data):
    num = data.get('num_arene')
    combatant_name = data['combatant']
    valeur = data['valeur']

    # Mise à jour du score
    combatant_arene[num][combatant_name]['score'] += valeur
    updated_score = combatant_arene[num][combatant_name]['score']

    # Notification au client pour la mise à jour
    emit('score_updated', {'combatant': combatant_name, 'score': updated_score}, broadcast=True)




if __name__ == '__main__':
    # L'application écoute sur toutes les interfaces réseau (0.0.0.0) sur le port 5000
    socketio.run(app, host='0.0.0.0', port=5000)
