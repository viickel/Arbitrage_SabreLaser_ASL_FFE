

class Arene(object):
	"""docstring for Arene"""
	def __init__(self, arg):
		super(Arene, self).__init__()
		self.combattants = {
			"rouge":
			"vert":
		}
		self.score = {
			"rouge":0
			"vert":0
		}
		self.cartons = {
			"rouge":{
				"blanc":0
				"jaune":0
				"rouge":0
			}
			"vert":{
				"blanc":0
				"jaune":0
				"rouge":0
			}
		}
		# TODO
		# self.chrono
		# self.statut = "en attente"
		# self.historique = []

		
	def ajouterCarton(self, combattant, couleur):
		self.cartons[combattant][couleur] += 1

	def incrementerScore(self, combattant, increment):
		self.score[combattant] += increment

	def vainqueur(self):
		# vérifier que la fin du match a eu lieu

		if self.score["rouge"] > self.score["vert"]:
			return  f"Combattant rouge : {self.combattants["rouge"].nom}"
		elif self.score["rouge"] < self.score["vert"]:
			return  f"Combattant vert : {self.combattants["vert"].nom}"
		else:
			return "Match nul"
