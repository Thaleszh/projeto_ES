
classes = list()

def saveClass(classToAdd):
	found = 0
	for index, classInList in classes:
		if classInList.getName() == classToAdd.getName(name):
			classes[index] = classToAdd
			found = 1
	if found == 0:
		classes.append(classToAdd)

def getClass(name):
	for classInList in classes:
		if classInList.getName() == name:
			return classInList
	return "notFound"

