from flask import Flask, render_template, request, jsonify

from models import *

app = Flask(__name__)

# Déclaration de l'objet Competition
# contenant une liste d'arènes
arenes = [None] + [Arene(x+1, Combattant(f"Rouge{x+1}"), Combattant(f"Vert{x+1}")) for x in range(5)]
competition = Competition(arenes)

@app.route('/affichage/<int:id_arene>')
def affichage(id_arene):
    return render_template('affichage.html', 
        arene=competition.arenes[id_arene])

@app.route('/bandeau/<int:id_arene>')
def bandeau(id_arene):
    return render_template('bandeau.html', 
        arene=competition.arenes[id_arene])

@app.route('/Arene/<int:id_arene>')
def arene(id_arene):
    return render_template('arbitrage.html', 
        arene=competition.arenes[id_arene])

################### Routes pour l'arbitrage ###################
@app.route('/increment-score/<int:id_arene>/<combattant>/<int:valeur>', methods=['POST'])
def incrementScore(id_arene, combattant, valeur):
    # quand il y aura plusieurs arènes, il faudra un paramètre id_arene
    last_action = competition.arenes[id_arene].incrementerScore(combattant, valeur)
    return jsonify(arene=competition.arenes[id_arene].to_json()) 

@app.route('/increment-carton/<int:id_arene>/<combattant>/<couleur>', methods=['POST'])
def incrementCarton(id_arene, combattant, couleur):
    # quand il y aura plusieurs arènes, il faudra un paramètre id_arene
    last_action = competition.arenes[id_arene].ajouterCarton(combattant, couleur)
    return jsonify(arene=competition.arenes[id_arene].to_json())

@app.route('/annuler/<int:id_arene>', methods=['POST'])
def annulerAction(id_arene):
    if len(competition.arenes[id_arene].historique) == 0:
        return jsonify(arene=competition.arenes[id_arene].to_json())
    
    competition.arenes[id_arene].annulerDerniereAction()
    return jsonify(arene=competition.arenes[id_arene].to_json())

################### Routes pour l'affichage ###################
@app.route('/score/<int:id_arene>', methods=['POST'])
def score(id_arene):
    # TODO : renvoyer l'objet arene et adapter l'affichage
    # return jsonify(arene=competition.arenes[id_arene].to_json())
    return jsonify(score=competition.arenes[id_arene].score)

if __name__ == '__main__':
    # L'application écoute sur toutes les interfaces réseau (0.0.0.0) sur le port 5000
    app.run(debug=True)
