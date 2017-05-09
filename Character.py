from Tag import Tag
from Class import Class

class Character:

#Atributes
    def __init__(self, name, class):
        self.name = name
        self.creator = user
        self.tags = set()
        self.edition = 0
        self.atributes = list()
        self.inventory = list()
        self.description = ""
        self.level = 1
        self.experience = 0

#add a name
    def setName(self, user, newName):
        if (self.checkPermition(user)):
            self.name = newName

    def getName(self):
        return self.name

#add a player
    def setCreator(self, user, newCreator):
        if (self.checkPermition(user)):
            self.creator = newCreator

    def getCreator(self):
        return self.creator

#add a tag
    def addTag(self, user, tag):
        if (self.checkPermition(user)):
            self.tags.append(tag)

    def delTag(self, user, tag):
        if (self.checkPermition(user)):
            self.tags.discard(tag)

    def getTags(self):
        return tags

#change atributes
    def setAtributes(self, user, atributes):
        if (self.checkPermition(user)):
            self.atributes = atributes

    def getAtributes(self):
        return self.atributes

#change experience
    def setExperience(self, user, value):
        if (self.checkPermition(user)):
            self.experience = value

    def getExperience(self):
        return self.experience

    def addExperience(self, user, value):
        if (self.checkPermition(user)):
            self.experience += value

#modify inventory

    def setInventory(self, user, newIventory):
        if (self.checkPermition(user)):
            self.inventory = newIventory

    def getInventory(self):
        return self.inventory

    def addItem(self, user, item):
        if (self.checkPermition(user)):
            self.inventory.append(item)

#change level

    def setLevel(self, user, value):
        if (self.checkPermition(user)):
            self.level = value

    def getLevel(self):
        return self.level

    def gainLevel(self, user):
        if (self.checkPermition(user)):
            self.level += 1

#description
    def setDescription(self, user, text):
        if (self.checkPermition(user)):
            self.description = text

    def getDescription(self):
        return self.description

#check if the user has permition
    def checkPermition(self, user):
        if(self.edition):
            return 1
        if (self.creator == user):
            self.edition = 1
            return 1
        return 0

    def close(self):
        self.edition = 0

    def checkCreator(self, user):
        return self.creator == user
