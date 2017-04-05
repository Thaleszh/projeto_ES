from Ability import Ability
class Class:

#Atributes
	name = ""
	tags = set()
	edition = 0
	colaborators = set()
	abilities = list()
	creator = 0

	def __init__(self, name, user):
		self.name = name
		self.creator = user

#add a name
	def setName(newName):
		self.name = newName

	def getName(self):
		return self.name

#add a tag
	def addTag(self, user, tag):
		if (self.checkPermition(user)):
			self.tags.append(tag)
	def delTag(self, user, tag):
		if (self.checkPermition(user)):
			self.tags.discard(tag)

#add an ability with its description
	def addAbility(self, user, abilityName, description):
		if (self.checkPermition(user)):
			newAbility = Ability(abilityName, description)
			self.abilities.append(newAbility)

	def editAbility(self, user, abilityName, description):
		if (self.checkPermition(user)):
			ability = searchAbility(abilityName)
			self.ability.setDescription(description)

	def delAbility(self, user, abilityName):
		if (self.checkPermition(user)):
			ability = searchAbility(abilityName)
			self.abilities.remove(ability)

	def searchAbility(self, abilityName):
		for ability in self.abilities:
			if ability.getName() == abilityName:
				return ability

	def getAbilities(self):
		return self.abilities

#add an colaborator to permition list
	def addColaborator(self, user, colaborator):
		if (self.checkCreator(user)):
			self.colaborator.append(colaborator)

	def delColaborator(self, user, colaborator):
		if (self.checkCreator(user)):
			self.colaborators.discard(colaborator)

#check if the user has permition
	def checkPermition(self, user):
	    if(self.edition):
	        return 1
	    if (self.creator == user):
	    	edition = 1
	    	return 1
	    if(user in self.colaborators):
	    	edition = 1
	    	return 1
	    return 0

	def checkCreator(self, user):
		return self.creator == user
