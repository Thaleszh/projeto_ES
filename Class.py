
class Class:

#Atributes
tags = set{}
colaborators = set{}
creator

#add a tag
	def addTag(user, tag):
		if (checkPermition(user)):
			tags.append(tag)
	def delTag(user, tag):
		if (checkPermition(user)):
			tags.discard(tag)

#add an ability with its description
	def addAbility():
		if (checkPermition(user)):

	def delAbility():
		if (checkPermition(user)):

#add an colaborator to permition list
	def addColaborator():
	def delColaborator(user, colaborator):
		if (checkCreator(user)):
			colaborators.discard(colaborator)

#check if the user has permition
	def checkPermition(user):
	    if(edition):
	        return 1
	    if(user in colaborators):
	    	edition = 1
	    	return 1                                                                                                                                                                                                                          6
	    return 0

	def checkCreator(user):
		return creator == user

     

