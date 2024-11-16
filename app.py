from flask import Flask, render_template, request, jsonify
import time

from models import *

app = Flask(__name__)

# Déclaration de l'objet Arène
# (à terme, il s'agira d'une liste d'arènes)
combattant_rouge = Combattant("Atom")
combattant_vert = Combattant("Zeus")
arena = Arene(1, combattant_rouge, combattant_vert)

@app.route('/affichage/<string:num>')
def affichage(num: str):
    return render_template('affichage.html', arene=arena)

@app.route('/bandeau/<string:num>')
def bandeau(num: str):
    return render_template('bandeau.html', arene=arena)

@app.route('/Arene/<string:num>')
def arene(num: str):
    return render_template('arbitrage.html', arene=arena)



if __name__ == '__main__':
    # L'application écoute sur toutes les interfaces réseau (0.0.0.0) sur le port 5000
    app.run(debug=True)
