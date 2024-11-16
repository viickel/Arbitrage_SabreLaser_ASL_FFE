from flask import Flask, render_template, request, jsonify
from datetime import datetime

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

    # on garde un historique des actions effectuées
    t = datetime.now().time()
    timestamp = f"{t.hour}:{t.minute}:{t.second:02}"
    arena.historique.append((timestamp, combattant, valeur, "point(s)"))
    last_action = f"[{arena.historique[-1][0]}] {arena.historique[-1][1]}: {arena.historique[-1][2]} {arena.historique[-1][3]}"
    return jsonify(score=arena.score, last_action=last_action)

@app.route('/increment-carton/<combattant>/<couleur>', methods=['POST'])
def incrementCarton(combattant, couleur):
    # quand il y aura plusieurs arènes, il faudra un paramètre id_arene
    
    # on ajoute un carton
    arena.cartons[combattant][couleur] += 1
    # pour les cartons au-dessus du blanc, le score change
    if couleur != "blanc":
        adversaire = "vert" if combattant == "rouge" else "rouge"
        arena.score[adversaire] += 3

    # on garde un historique des actions effectuées
    t = datetime.now().time()
    timestamp = f"{t.hour}:{t.minute}:{t.second}"
    arena.historique.append((timestamp, combattant, "carton", couleur))
    last_action = f"[{arena.historique[-1][0]}] {arena.historique[-1][1]}: {arena.historique[-1][2]} {arena.historique[-1][3]}"
    return jsonify(cartons=arena.cartons, score=arena.score, last_action=last_action)

@app.route('/annuler', methods=['POST'])
def annulerAction():
    pass

################### Routes pour l'affichage ###################
@app.route('/score/<int:num>', methods=['POST'])
def score(num):
    # TODO : utiliser num pour changer d'arène
    return jsonify(score=arena.score)

if __name__ == '__main__':
    # L'application écoute sur toutes les interfaces réseau (0.0.0.0) sur le port 5000
    app.run(debug=True)
