class Table:
    def __init__(self, name, user):
        self.name = name
        self.lore = Log()
        self.log = Log()
        self.master = user
        self.players = list()
        self.characters = list()

    def addPlayer(master, player):
        if(self.master == master):
            self.players.append(player)
        else:
            Vision.display("You are not the game master")

    def delPlayer(master, player):
        if(self.master == master):
            self.players.remove(player)
        else:
            Vision.display("You are not the game master")

    def quit(player):
        self.player.remove(player)

    def delCharacter(master, char):
        if(self.master == master):
            self.characters.remove(char)
        else:
            Vision.display("You are not the game master")

    def addCharacter(master, char):
        if(self.master == master and char.getCreator in self.players):
            self.characters.append(char)
        else:
            Vision.display("You are not the game master or character invalid")
