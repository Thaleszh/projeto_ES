
classes = list()

def saveClass(classToAdd):
	classe = getClass(classToAdd)
	if classe == "notFound":
		classes.append(classToAdd)
	else:
		classes[index(classe)] = classToAdd

def getClass(name):
	for classInList in classes:
		if classInList.getName() == name:
			return classInList
	return "notFound"

def removeClass(name):
	classes.remove(name)

