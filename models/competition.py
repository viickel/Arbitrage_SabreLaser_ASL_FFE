

class Competition(object):
	"""docstring for Competition"""
	def __init__(self, arenes=[]):
		super(Competition, self).__init__()
		self.arenes = arenes

		# pour des configurations futures
		self.combattants = []
		self.matchs = []

	def ajouterArene(self, arene): 
		self.arenes.append(arene)

	def supprimerArene(self, num_arene: int):
		return self.arenes.pop(num_arene)
	
	@classmethod
	def importerConfiguration(cls, file): pass