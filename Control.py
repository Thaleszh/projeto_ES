from Class import Class
from Table import Table
import Vision
import Persistencia
user = 1

def addClass():
    name = Vision.entry("Class name: ")
    newClass = Class(name, user)
    Persistencia.saveClass(newClass)

def addAbility():
    name = Vision.entry("Class name: ")
    tempClass = Persistencia.getClass(name)
    keep = 1
    while (keep == 1):
        abilityName = Vision.entry("Ability name: ")
        abilityDescription = Vision.entry("Ability Description: ")
        tempClass.addAbility(user, abilityName, abilityDescription)
        keep = int(Vision.entry("Do you wish to keep adding abilities?\n 1- Yes \n 2- No\n"))
    Persistencia.saveClass(tempClass)

def addColaborator():
    name = Vision.entry("Class name: ")
    classe = Persistencia.getClass(name)

def searchTag():
    name = Vision.entry("Class name: ")
    classe = Persistencia.getClass(name)
    displayClass(classe)

def displayClass(classe):
	Vision.display("\nClasse - " + classe.getName() + ": \n--------------\nAbilites:")
	for ability in classe.getAbilities():
		Vision.display(ability.getName()+": " + ability.getDescription())

def changeName():
    old = Vision.entry("Class to change name: ")
    new = Vision.entry("New Class Name: ")
    classe = Persistencia.getClass(old)
    Persistencia.delClass(classe)
    classe.setName(new)
    Persistencia.saveClass(classe)

def duplicateClass():
    old = Vision.entry("Name of the class to duplicate: ")
    new = Vision.entry("New Class Name: ")
    classe = Persistencia.getClass(old)
    classe.setName(new)
    Persistencia.saveClass(classe)

def delClass():
    classe = Vision.entry("Name of the class to be deleted: ")
    Persistencia.delClass(classe)

def createTable():
    name = Vision.entry("Table name: ")
    newTable = Table(name, user)
    Persistencia.saveTable(newTable)

def delTable():
    name = Vision.entry("Table name: ")
    Persistencia.delTable(name)

def editTable():
    option = Vision.entry("\n1 - Add Character\n2 - Remove Character\n3 - Add PLayer\n4 - Remove Player\n5 - Quit\n")
    cases[option]()

cases = {1 : caseAddC, 2 : caseDelC, 3 : caseAddP, 4 : caseDelP, 5 : caseQuit}

def caseAddC():
    name = Vision.entry("Table name: ")
    table = Persistencia.getTable(name)
    playerName = Vision.entry("Player name: ")
    player = Persistencia.getUser(playerName)
    charName = Vision.entry("Character name: ")
    char = player.getCharacter(charName)
    table.addCharacter(user, char)

def caseDelC():
    name = Vision.entry("Table name: ")
    table = Persistencia.getTable(name)
    playerName = Vision.entry("Player name: ")
    player = Persistencia.getUser(playerName)
    charName = Vision.entry("Character name: ")
    char = player.getCharacter(charName)
    table.delCharacter(user, char)

def caseAddP():
    name = Vision.entry("Table name: ")
    table = Persistencia.getTable(name)
    playerName = Vision.entry("Player name: ")
    player = Persistencia.getUser(playerName)
    table.addPlayer(user, player)

def caseDelP():
    name = Vision.entry("Table name: ")
    table = Persistencia.getTable(name)
    playerName = Vision.entry("Player name: ")
    player = Persistencia.getUser(playerName)
    table.delPlayer(user, player)

def caseQuit():
    name = Vision.entry("Table name: ")
    table = Persistencia.getTable(name)
    table.quit(player)

def editLog():
    name = Vision.entry("Table name: ")
    table = Persistencia.getTable(name)
    option = Vision.entry("\n1 - Edit Lore\n2 - Edit Log\n")
    if option == 1:
        lore = table.getLore()
        Vision.display(lore)
        lore = Vision.entry("Type the new lore: ")
        table.setLore(lore)
        Persistencia.saveTable(table)
    else:
        log = table.getLog()
        Vision.display(log)
        log = Vision.entry("Type the new log: ")
        table.setLore(log)
        Persistencia.saveTable(table)
