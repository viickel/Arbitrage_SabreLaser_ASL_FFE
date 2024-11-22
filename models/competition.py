

class Competition(object):
	"""docstring for Competition"""
	def __init__(self, arenes=[]):
		super(Competition, self).__init__()
		self.arenes = arenes

		# pour des configurations futures
		self.combattants = []
		self.matchs = []

	def ajouterArene(self, arene): pass
	def supprimerArene(self, num_arene: int): pass
	@classmethod
	def importerConfiguration(cls, file): pass