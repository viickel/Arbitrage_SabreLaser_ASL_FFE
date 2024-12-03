

class Combattant(object):
	"""docstring for Combattant"""
	def __init__(self, nom, license=None, points_quest=0):
		super(Combattant, self).__init__()
		self.nom = nom
		self.license = license
		# self.categorie # TODO
		self.points_quest = points_quest


	def to_json(self):
		d = {}
		d["nom"] = self.nom
		d["license"] = self.license
		d["points_quest"] = self.points_quest
		return d