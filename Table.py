from Log import Log

class Table:
    def __init__(self, name, user):
        self.name = name
        self.lore = Log("","")
        self.log = Log("","")
        self.master = user
        self.players = list()
        self.characters = list()
        self.edition = 0

    def addPlayer(self, master, player):
        if(self.checkPermition(master)):
            self.players.append(player)
        else:
            Vision.display("You are not the game master")

    def delPlayer(self, master, player):
        if(self.checkPermition(master)):
            self.players.remove(player)
        else:
            Vision.display("You are not the game master")

    def quit(self, player):
        self.player.remove(player)

    def delCharacter(self, master, char):
        if(self.checkPermition(master)):
            self.characters.remove(char)
        else:
            Vision.display("You are not the game master")

    def addCharacter(self, master, char):
        if(self.checkPermition(master) or char.getCreator in self.players):
            self.characters.append(char)
        else:
            Vision.display("You are not the game master or character invalid")

    def checkPermition(self, user):
        if(self.edition):
            return 1
        if (self.master == user):
            edition = 1
            return 1
        return 0

    def close(self):
        self.edition = 0

    def getName(self):
        return self.name

    def getLog(self):
        return self.log

    def setLog(self, newLog):
        self.log = newLog

    def getLore(self):
        return self.lore

    def setLore(self, newLore):
        self.lore = newLore

    def getMaster(self):
        return self.master
