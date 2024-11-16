from flask import Flask, render_template, request, jsonify
import time

from models import *

app = Flask(__name__)

# Déclaration de l'objet Arène
# (à terme, il s'agira d'une liste d'arènes)
combattant_rouge = Combattant("Atom")
combattant_vert = Combattant("Zeus")
arena = Arene(1, combattant_rouge, combattant_vert)

@app.route('/affichage/<int:num>')
def affichage(num):
    return render_template('affichage.html', arene=arena)

@app.route('/bandeau/<int:num>')
def bandeau(num):
    return render_template('bandeau.html', arene=arena)

@app.route('/Arene/<int:num>')
def arene(num):
    return render_template('arbitrage.html', arene=arena)

################### Routes pour l'arbitrage ###################
@app.route('/increment-score/<combattant>/<int:valeur>', methods=['POST'])
def incrementScore(combattant, valeur):
    # quand il y aura plusieurs arènes, il faudra un paramètre id_arene
    arena.score[combattant] += valeur
    return jsonify(score=arena.score)

@app.route('/increment-carton/<combattant>/<couleur>', methods=['POST'])
def incrementCarton(combattant, couleur):
    # quand il y aura plusieurs arènes, il faudra un paramètre id_arene
    arena.cartons[combattant][couleur] += 1
    return jsonify(cartons=arena.cartons)


################### Routes pour l'affichage ###################
@app.route('/score/<int:num>', methods=['POST'])
def score(num):
    # TODO : utiliser num pour changer d'arène
    return jsonify(score=arena.score)

if __name__ == '__main__':
    # L'application écoute sur toutes les interfaces réseau (0.0.0.0) sur le port 5000
    app.run(debug=True)
