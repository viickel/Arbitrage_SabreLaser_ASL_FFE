

class Combattant(object):
	"""docstring for Combattant"""
	def __init__(self, nom, license=None, points_quest=0):
		super(Combattant, self).__init__()
		self.nom = nom
		self.license = license
		# self.categorie # TODO
		self.points_quest = points_quest
