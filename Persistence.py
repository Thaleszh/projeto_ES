
classes = list()
characters = list()
tables = list()
openTables = list()

def saveClass(classToAdd):
	classe = getClass(classToAdd.getName())
	if classe == "notFound":
		classes.append(classToAdd)
	else:
		classes[classes.index(classe)] = classToAdd

def getClass(name):
	for classInList in classes:
		if classInList.getName() == name:
			return classInList
	return "notFound"

def delClass(name):
	for classInList in classes:
		if classInList.getName() == name:
			classes.remove(classInList)
			break

def addOpenTable(table):
	table = getTable(table.getName())
	if table == "notFound":
		openTables.append(table)
	else:
		openTables[openTables.index(table)] = table

def delOpenTable(name):
	for table in openTables:
		if openTables.getName() == name:
			openTables.remove(table)
			break

def getTable(name):
	for table in tables:
		if table.getName() == name:
			return table
	return "notFound"

def saveTable(table):
	table = getTable(table.getName())
	if table == "notFound":
		tables.append(table)
	else:
		tables[tables.index(table)] = table

def delTable(name):
	for table in tables:
		if tables.getName() == name:
			tables.remove(table)
			break
