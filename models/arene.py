from datetime import datetime

class Arene(object):
	"""docstring for Arene"""
	def __init__(self, numero, combattant_rouge, combattant_vert):
		super(Arene, self).__init__()
		self.numero = numero
		self.combattants = {
			"rouge":combattant_rouge,
			"vert":combattant_vert
		}
		self.score = {
			"rouge":0,
			"vert":0
		}
		self.cartons = {
			"rouge":{
				"blanc":0,
				"jaune":0,
				"rouge":0
			},
			"vert":{
				"blanc":0,
				"jaune":0,
				"rouge":0
			}
		}
		self.historique = []
		# TODO
		# self.chrono
		# self.statut = "en attente"

		
	def ajouterCarton(self, combattant, couleur):
		# on ajoute un carton
		self.cartons[combattant][couleur] += 1
		# pour les cartons au-dessus du blanc, le score change
		if couleur != "blanc":
			adversaire = "vert" if combattant == "rouge" else "rouge"
			self.score[adversaire] += 3

		# on garde un historique des actions effectuées
		t = datetime.now().time()
		timestamp = f"{t.hour}:{t.minute}:{t.second}"
		self.historique.append((timestamp, combattant, "carton", couleur))

	def incrementerScore(self, combattant, increment):
		self.score[combattant] += increment

		# on garde un historique des actions effectuées
		t = datetime.now().time()
		timestamp = f"{t.hour}h{t.minute}:{t.second:02}"
		self.historique.append((timestamp, combattant, increment, "point(s)"))

	def annulerDerniereAction(self):
		last_action = self.historique[-1]
		if last_action[2] == "carton":
			# Dans le cas d'un carton, il faut enlever le carton
			# et baisser le score de l'adversaire si ce n'est pas
			# un carton blanc
			_, combattant, _, couleur = last_action
			self.cartons[combattant][couleur] -= 1
			if couleur != "blanc":
				adversaire = "vert" if combattant == "rouge" else "rouge"
				self.score[adversaire] -= 3
			self.historique.pop(-1)
		elif last_action[3] == "point(s)":
			# Dans le cas d'un ajout de point
			# on diminue simplement le score de la valeur
			_, combattant, valeur, _ = last_action
			self.score[combattant] -= valeur
			self.historique.pop(-1)

	def vainqueur(self):
		# vérifier que la fin du match a eu lieu

		if self.score["rouge"] > self.score["vert"]:
			return  f"Combattant rouge : {self.combattants["rouge"].nom}"
		elif self.score["rouge"] < self.score["vert"]:
			return  f"Combattant vert : {self.combattants["vert"].nom}"
		else:
			return "Match nul"
