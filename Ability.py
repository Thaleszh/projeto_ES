class Ability:

#atributes
	name = ""
	description = ""

	def __init__(self, name, description):
		self.name = name
		self.description = description

	def setName(self, newName):
		self.name = newName

	def getName(self):
		return self.name

	def setDescription(self, text):
		self.description = text

	def getDescription(self):
		return self.description