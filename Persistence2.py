classes = list()
characters = list()
tables = list()
openTables = list()
users = list()

def saveClass(classToAdd):
	if classToAdd not in classes:
		classes.append(classToAdd)
	else:
		classes[classes.index(classToAdd)] = classToAdd

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

def saveUser(userToAdd):
	if userToAdd not in users:
		users.append(userToAdd)
	else:
		users[users.index(userToAdd)] = userToAdd

def getUser(name):
	for user in users:
		if user.getName() == name:
			return user
	return "notFound"

def delUser(name):
	for user in users:
		if users.getName() == name:
			users.remove(user)
			break

def addOpenTable(table):
	if table not in openTables:
		openTables.append(table)
	else:
		openTables[openTables.index(table)] = table

def delOpenTable(name):
	for table in openTables:
		if table.getName() == name:
			openTables.remove(table)
			break

def getTable(name):
	for table in tables:
		if table.getName() == name:
			return table
##	return "notFound"

def saveTable(table):
	if table not in tables:
		tables.append(table)
	else:
		tables[tables.index(table)] = table

def delTable(name):
	for table in tables:
		if table.getName() == name:
			tables.remove(table)
			break

def getCharacter(name):
	for character in characters:
		if character.getName() == name:
			return character
	return "notFound"

def saveCharacter(character):
	if character not in characters:
		characters.append(character)
	else:
		characters[characters.index(character)] = character

def delCharacter(name):
	for character in characters:
		if characters.getName() == name:
			characters.remove(character)
			break
