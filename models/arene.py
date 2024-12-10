from datetime import datetime

class Arene(object):
	"""docstring for Arene"""
	def __init__(self, _id, combattant_rouge, combattant_vert, chrono):
		super(Arene, self).__init__()
		self._id = _id
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
		self.historique = [] # TODO: créer un objet log
		self.last_action_msg = ""
		self.chrono = chrono
		
	def ajouterCarton(self, combattant, couleur):
		# on ajoute un carton
		self.cartons[combattant][couleur] += 1
		
		adversaire = "vert" if combattant == "rouge" else "rouge"
		# pour les cartons au-dessus du blanc, le score change
		if couleur == "blanc":
			# [TODO issue#3]
			# # au delà de 1 carton blanc, on accorde 3pts à l'adversaire
			# # à chaque nouveau carton
			# if self.cartons[combattant][couleur] >= 2:
			# 	self.score[adversaire] += 3 
			pass
		elif couleur == "jaune":
			# carton jaune = 3pts pour l'adversaire
			self.score[adversaire] += 3
		elif couleur == "rouge":
			# carton rouge = 5pts pour l'adversaire
			self.score[adversaire] += 5

		# on garde un historique des actions effectuées
		t = datetime.now().time()
		timestamp = f"{t.hour:02}h{t.minute:02}:{t.second:02}"
		self.historique.append((timestamp, combattant, "carton", couleur))
		self.last_action_msg = f"[{self.historique[-1][0]}] {self.historique[-1][1]}:"
		self.last_action_msg += f" {self.historique[-1][2]} {self.historique[-1][3]}"

	def incrementerScore(self, combattant, increment):
		self.score[combattant] += increment

		# on garde un historique des actions effectuées
		t = datetime.now().time()
		timestamp = f"{t.hour:02}h{t.minute:02}:{t.second:02}"
		self.historique.append((timestamp, combattant, increment, "point(s)"))
		self.last_action_msg = f"[{self.historique[-1][0]}] {self.historique[-1][1]}:"
		self.last_action_msg += f" {self.historique[-1][2]} {self.historique[-1][3]}"
		return self.last_action_msg

	def annulerDerniereAction(self):
		last_action = self.historique[-1]
		if last_action[2] == "carton":
			# Dans le cas d'un carton, il faut enlever le carton
			# et baisser le score de l'adversaire si ce n'est pas
			# un carton blanc
			_, combattant, _, couleur = last_action
			self.cartons[combattant][couleur] -= 1

			adversaire = "vert" if combattant == "rouge" else "rouge"
			if couleur == "blanc":
				# [TODO issue#3]
				pass
			elif couleur == "jaune":
				self.score[adversaire] -= 3
			elif couleur == "rouge":
				self.score[adversaire] -= 5

			self.historique.pop(-1)
		elif last_action[3] == "point(s)":
			# Dans le cas d'un ajout de point
			# on diminue simplement le score de la valeur
			_, combattant, valeur, _ = last_action
			self.score[combattant] -= valeur
			self.historique.pop(-1)

		if len(self.historique) > 0:
			self.last_action_msg = f"[{self.historique[-1][0]}] {self.historique[-1][1]}:"
			self.last_action_msg += f" {self.historique[-1][2]} {self.historique[-1][3]}"
		else:
			self.last_action_msg = ""
		return self.last_action_msg

	def to_json(self):
		d = {}
		d["_id"] = self._id
		d["combattants"] = {
			"rouge":self.combattants["rouge"].to_json(),
			"vert":self.combattants["vert"].to_json()
			}
		d["score"] = self.score
		d["cartons"] = self.cartons
		d["historique"] = self.historique
		d["last_action_msg"] = self.last_action_msg
		d["remaining_time"] = self.chrono.remainingTime()
		return d

	def reset(self):
		self.combattants["rouge"].nom = f"Rouge{self._id}"
		self.combattants["vert"].nom = f"Vert{self._id}"
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
		self.last_action_msg = ""
