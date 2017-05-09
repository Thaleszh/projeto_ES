class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.characters = list()
        self.tables = list()
        self.classes = list()

    def getName():
        return self.name

    def setName(newName):
        if (self.checkpermition(user)):
            self.name = newName

    def getPassword():
        return self.password

    def setPassword(newPass):
        if (self.checkpermition(user)):      
            self.password = newPass

# get classe
    def getClasses(self):
        return self.classes

    def setClasses(self, user, newClasses):
        if (self.checkpermition(user)):
            self.classes = newClasses

    def addClass(self, user, newClass):
        if (self.checkpermition(user)):
            if newClass not in self.classes: 
                self.classes.append(newClass)

    def delClass(self, user, oldClass):
        if (self.checkpermition(user)):
            if oldClass in self.classes: 
                self.classes.remove(oldClass)

# get table
    def getTables(self):
        return self.tables

    def setTables(self, user, newTables):
        if (self.checkpermition(user)):
            self.tables = newTables

    def addTable(self, user, newTable):
        if (self.checkpermition(user)):
            if newTable not in self.tables: 
                self.tables.append(newTable)

    def delTable(self, user, oldTable):
        if (self.checkpermition(user)):
            if oldTable in self.tables: 
                self.tables.remove(oldTable)

# get characters
    def getCharacters(self):
        return self.characters

    def setCharacters(self, user, newCharacters):
        if (self.checkpermition(user)):
            self.characters = newCharacters

    def addCharacter(self, user, newCharacter):
        if (self.checkpermition(user)):
            if newCharacters not in self.characters: 
                self.characters.append(newCharacters)

    def delCharacter(self, user, oldCharacter):
        if (self.checkpermition(user)):
            if oldCharacter in self.characters: 
                self.characters.remove(oldCharacter)


# check permition
    def checkPermition(self, user):
        if (self == user):
            return 1
        return 0
