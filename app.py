from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit  # type: ignore
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Déclaration du dictionnaire de données Combat 
# Il est composé de 2 sous-dictionnaires : 'Rouge' et 'Vert' avec leurs scores et pénalités
combattant = { 
    'Rouge': {'score': 0, 'cartons_blanc': 0, 'cartons_jaune': 0, 'cartons_rouge': 0, 'nom': 'Combattant Rouge', 'Num_Licence': 0,'Quest':0},
    'Vert': {'score': 0, 'cartons_blanc': 0, 'cartons_jaune': 0, 'cartons_rouge': 0, 'nom': 'Combattant Vert', 'Num_Licence': 0,'Quest':0}
}

# Dictionnaire pour stocker les données de chaque arène
combattant_arene = {}

# Fonction d'initialisation pour créer une arène si elle n'existe pas déjà
def init_combattant_arene(num):
     if num not in combattant_arene:
          # Clone le modèle de combattant pour l'arène donnée
          combattant_arene[num] = {
               'Rouge': combattant['Rouge'].copy(),
               'Vert' : combattant['Vert'].copy()
          }

@app.route('/affichage/<string:num>')
def affichage(num: str):
    init_combattant_arene(num)
    return render_template('affichage.html', num_arene=num, combattant=combattant_arene[num])

@app.route('/bandeau/<string:num>')
def bandeau(num: str):
    init_combattant_arene(num)
    return render_template('bandeau.html', num_arene=num, combattant=combattant_arene[num])

@app.route('/Arene/<string:num>')
def arene(num: str):
    init_combattant_arene(num)
    return render_template('arbitrage.html', num_arene=num, combattant=combattant_arene[num])


@socketio.on('maj_score')
def handle_maj_score(data):
    num = data.get('num_arene')
    combattant_name = data['combattant']
    valeur = data['valeur']

    # Mise à jour du score
    combattant_arene[num][combattant_name]['score'] += valeur
    updated_score = combattant_arene[num][combattant_name]['score']

    # Notification au client pour la mise à jour
    emit('score_updated', {'combattant': combattant_name, 'score': updated_score}, broadcast=True)



if __name__ == '__main__':
    # L'application écoute sur toutes les interfaces réseau (0.0.0.0) sur le port 5000
    socketio.run(app, host='0.0.0.0', port=5000)
