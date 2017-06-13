class Log:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription
