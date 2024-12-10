from datetime import datetime, timedelta

class Chronometre(object):
	"""docstring for Chronometre"""
	def __init__(self, base_time):
		super(Chronometre, self).__init__()
		self.end_time = None
		self.state = "stopped"
		self.base_time = base_time
		self._banked = base_time
	
	def start(self):
		self.end_time = datetime.now() + timedelta(seconds=self._banked)
		self.state = "running"

	def pause(self):
		self.state = "paused"
		now = datetime.now()
		self._banked = int((self.end_time - now).total_seconds())

	def reset(self):
		self.state = "stopped"
		self._banked = self.base_time
		self.end_time = None
		
	def addSeconds(self, sec):
		if self.state in ("stopped", "paused"):
			self._banked += sec
		elif self.state == "running":
			self.end_time += timedelta(seconds=sec)

	def subSeconds(self, sec):
		if self.state in ("stopped", "paused"):
			self._banked -= sec
		elif self.state == "running":
			self.end_time -= timedelta(seconds=sec)

	def remainingTime(self):
		if self.state == "stopped":
			return self._banked
		elif self.state == "running":
			now = datetime.now()
			remaining = (self.end_time - now).total_seconds()
			return max(0, int(remaining))
		elif self.state == "paused":
			print(self._banked)
			return self._banked
