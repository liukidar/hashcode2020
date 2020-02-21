class Book:
	def __init__(self, _id, _score):
		self.id = _id
		self.score = _score
		self.n = 0

	def addCopy(self):
		self.n += 1

	def value(self):
		return self.score / self.n