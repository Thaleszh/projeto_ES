class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.characters = list()
        self.tables = list()
        self.classes = list()

    def getName(self):
        return self.name

    def setName(self, newName):
        if (self.checkPermition(user)):
            self.name = newName

    def getPassword(self):
        return self.password

    def setPassword(self, newPass):
        if (self.checkPermition(user)):
            self.password = newPass

# get classe
    def getClasses(self):
        return self.classes

    def setClasses(self, user, newClasses):
        if (self.checkPermition(user)):
            self.classes = newClasses

    def addClass(self, user, newClass):
        if (self.checkPermition(user)):
            if newClass not in self.classes:
                self.classes.append(newClass)

    def delClass(self, user, oldClass):
        if (self.checkPermition(user)):
            if oldClass in self.classes:
                self.classes.remove(oldClass)

# get table
    def getTables(self):
        return self.tables

    def setTables(self, user, newTables):
        if (self.checkPermition(user)):
            self.tables = newTables

    def addTable(self, user, newTable):
        if (self.checkPermition(user)):
            if newTable not in self.tables:
                self.tables.append(newTable)

    def delTable(self, user, oldTable):
        if (self.checkPermition(user)):
            if oldTable in self.tables:
                self.tables.remove(oldTable)

# get characters
    def getCharacters(self):
        return self.characters

    def setCharacters(self, user, newCharacters):
        if (self.checkPermition(user)):
            self.characters = newCharacters

    def addCharacter(self, user, newCharacter):
        if (self.checkPermition(user)):
            if newCharacter not in self.characters:
                self.characters.append(newCharacter)

    def delCharacter(self, user, oldCharacter):
        if (self.checkPermition(user)):
            if oldCharacter in self.characters:
                self.characters.remove(oldCharacter)

    def getCharacter(self, name):
    	for character in self.characters:
    		if character.getName() == name:
    			return character
    	return "notFound"

# check permition
    def checkPermition(self, user):
        if (self == user):
            return 1
        return 0
