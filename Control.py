from Class import Class
from Table import Table
from User import User
from Character import Character

import Vision
import Persistence

def addClass(currentUser):
    name = Vision.entry("Class name: ")
    newClass = Class(name, currentUser)
    Persistence.saveClass(newClass)

def searchClass(name):
    displayClass(Persistence.getClass(name))

def addAbility(currentClass):
    keep = 1
    while (keep == 1):
        abilityName = Vision.entry("Ability name: ")
        abilityDescription = Vision.entry("Ability Description: ")
        currentClass.addAbility(currentUser, abilityName, abilityDescription)
        keep = int(Vision.entry("Do you wish to keep adding abilities?\n 1- Yes \n 2- No\n"))
    Persistence.saveClass(currentClass)

def displayClass(currentClass):
	Vision.display("\nClasse - " + currentClass.getName() + ": \n--------------\nAbilites:")
	for ability in currentClass.getAbilities():
		Vision.display(ability.getName()+": " + ability.getDescription())

def changeName():
    old = Vision.entry("Class to change name: ")
    new = Vision.entry("New Class Name: ")
    currentClass = Persistence.getClass(old)
    Persistence.delClass(currentClass)
    currentClass.setName(new)
    Persistence.saveClass(currentClass)

def duplicateClass():
    old = Vision.entry("Name of the class to duplicate: ")
    new = Vision.entry("New Class Name: ")
    currentClass = Persistence.getClass(old)
    currentClass.setName(new)
    Persistence.saveClass(currentClass)

def delClass():
    currentClass = Vision.entry("Name of the class to be deleted: ")
    Persistence.delClass(currentClass)

#Table
def createTable(currentUser):
    name = Vision.entry("Table name: ")
    newTable = Table(name, currentUser)
    Persistence.saveTable(newTable)

def delTable():
    name = Vision.entry("Table name: ")
    Persistence.delTable(name)

def editTable(option, currentTable):
    caseManageTable[option](currentTable)

# cases Manage Table
def caseAddC(currentTable):
    playerName = Vision.entry("Player name: ")
    player = Persistence.getUser(playerName)
    charName = Vision.entry("Character name: ")
    char = player.getCharacter(charName)
    table.addCharacter(currentUser, char)
    Persistence.saveTable(currentTable)

def caseDelC(currentTable):
    playerName = Vision.entry("Player name: ")
    player = Persistence.getUser(playerName)
    charName = Vision.entry("Character name: ")
    char = player.getCharacter(charName)
    currentTable.delCharacter(currentUser, char)
    Persistence.saveTable(currentTable)

def caseAddP(currentTable):
    playerName = Vision.entry("Player name: ")
    player = Persistence.getUser(playerName)
    currentTable.addPlayer(currentUser, player)
    Persistence.saveTable(currentTable)

def caseDelP(currentTable):
    playerName = Vision.entry("Player name: ")
    player = Persistence.getUser(playerName)
    currentTable.delPlayer(currentUser, player)
    Persistence.saveTable(currentTable)

def caseOpen(currentTable):
    name = currentTable.getName()
    Persistence.addOpenTable(table)

def caseClose(currentTable):
    name = currentTable.getName()
    Persistence.delOpenTable(name)

def caseQuit(currentTable):
    currentTable.quit(player)

def editLog(currentTable):
    option = Vision.entry("\n1 - Edit Lore \n2 - Show Lore\n3 - Edit Log\n4 - Show Log\n")
    if int(option) <= 2:
        lore = currentTable.getLore()
        Vision.display(lore.getDescription())
        if int(option) == 1:
            lore.setDescription(Vision.entry("Type the new lore: "))
            currentTable.setLore(lore)
            Persistence.saveTable(currentTable)
    else:
        log = currentTable.getLog()
        Vision.display(log.getDescription())
        if int(option) == 3:
            log.setDescription(Vision.entry("Type the new log: "))
            currentTable.setLore(log)
            Persistence.saveTable(currentTable)

caseManageTable = {'1' : caseAddC, '2' : caseDelC, '3' : caseAddP, '4' : caseDelP, '5' : caseOpen, '6' : caseClose, '7' : editLog}

#Character

def addCharacter(currentUser):
    name = Vision.entry("Character name: ")
    className = Vision.entry("Character Class: ")
    currentClass = Persistence.getClass(currentClassName)
    char = Character(name, currentClass, currentUser)
    currentUser.addCharacter(currentUser, char)
    Persistence.saveUser(currentUser)
    Persistence.saveCharacter(char)

def delCharacter(currentUser):
    name = Vision.entry("Character name: ")
    char = currentUser.getCharacter(name)
    currentUser.delCharacter(currentUser, char)
    Persistence.delCharacter(char)
    Persistence.saveUser(currentUser)

def editCharacter(option, currentChar, currentUser, item):
    caseManageCharacter[option](currentChar, currentUser, item)

#Cases Manage Character

def caseUp(currentChar, currentUser):
    currentChar.gainLevel(currentUser)
    Persistence.saveCharacter(currentChar)

def caseDown(currentChar, currentUser):
    currentChar.loseLevel(currentUser)
    Persistence.saveCharacter(currentChar)

def caseGainXP(currentChar, currentUser, number):
    currentChar.addExperience(number)
    Persistence.saveCharacter(currentChar)

def caseLoseXp(currentChar, currentUser, number):
    currentChar.loseExperience(number)
    Persistence.saveCharacter(currentChar)

def caseAddInv(currentChar, currentUser, item):
    currentChar.addItem(currentUser, item)
    Persistence.saveCharacter(currentChar)

def caseRemInv(currentChar, currentUser, item):
    currentChar.delItem(currentUser, item)
    Persistence.saveCharacter(currentChar)

def caseShowInv():
    Inv = Character.getInventory()
    for item in Inv:
        Visio.display(item)

def addUser(name, passw):
    Persistence.saveUser(User(name, passw))

caseManageCharacter = {'1' : caseUp, '2' : caseDown, '3' : caseGainXP, '4' : caseLoseXp, '5' : caseShowInv, '6' : caseAddInv, '7' : caseRemInv}
