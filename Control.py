from Class import Class
from Table import Table
from User import User
from Character import Character

import Vision
import Persistence2

def addClass(currentUser):
    name = Vision.entry("Class name: ")
    newClass = Class(name, currentUser)
    Persistence2.saveClass(newClass)

def searchClass(name):
    displayClass(Persistence2.getClass(name))

def addAbility(currentClass):
    keep = 1
    while (keep == 1):
        abilityName = Vision.entry("Ability name: ")
        abilityDescription = Vision.entry("Ability Description: ")
        currentClass.addAbility(currentUser, abilityName, abilityDescription)
        keep = int(Vision.entry("Do you wish to keep adding abilities?\n 1- Yes \n 2- No\n"))
    Persistence2.saveClass(currentClass)

def displayClass(currentClass):
    Vision.display("\nClasse - " + currentClass.getName() + ": \n--------------\nAbilites:")
    for ability in currentClass.getAbilities():
        Vision.display(ability.getName()+": " + ability.getDescription())

def changeName():
    old = Vision.entry("Class to change name: ")
    new = Vision.entry("New Class Name: ")
    currentClass = Persistence2.getClass(old)
    Persistence2.delClass(currentClass)
    currentClass.setName(new)
    Persistence2.saveClass(currentClass)

def duplicateClass():
    old = Vision.entry("Name of the class to duplicate: ")
    new = Vision.entry("New Class Name: ")
    currentClass = Persistence2.getClass(old)
    currentClass.setName(new)
    Persistence2.saveClass(currentClass)

def delClass():
    currentClass = Vision.entry("Name of the class to be deleted: ")
    Persistence2.delClass(currentClass)

#Table
def createTable(currentUser):
    name = Vision.entry("Table name: ")
    newTable = Table(name, currentUser)
    Persistence2.saveTable(newTable)

def delTable():
    name = Vision.entry("Table name: ")
    Persistence2.delTable(name)

def editTable(option, currentTable):
    caseManageTable[option](currentTable)

# cases Manage Table
def caseAddC(currentTable):
    playerName = Vision.entry("Player name: ")
    player = Persistence2.getUser(playerName)
    charName = Vision.entry("Character name: ")
    char = player.getCharacter(charName)
    table.addCharacter(currentUser, char)
    Persistence2.saveTable(currentTable)

def caseDelC(currentTable):
    playerName = Vision.entry("Player name: ")
    player = Persistence2.getUser(playerName)
    charName = Vision.entry("Character name: ")
    char = player.getCharacter(charName)
    currentTable.delCharacter(currentUser, char)
    Persistence2.saveTable(currentTable)

def caseAddP(currentTable):
    playerName = Vision.entry("Player name: ")
    player = Persistence2.getUser(playerName)
    currentTable.addPlayer(currentUser, player)
    Persistence2.saveTable(currentTable)

def caseDelP(currentTable):
    playerName = Vision.entry("Player name: ")
    player = Persistence2.getUser(playerName)
    currentTable.delPlayer(currentUser, player)
    Persistence2.saveTable(currentTable)

def caseOpen(currentTable):
    name = currentTable.getName()
    Persistence2.addOpenTable(table)

def caseClose(currentTable):
    name = currentTable.getName()
    Persistence2.delOpenTable(name)

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
            Persistence2.saveTable(currentTable)
    else:
        log = currentTable.getLog()
        Vision.display(log.getDescription())
        if int(option) == 3:
            log.setDescription(Vision.entry("Type the new log: "))
            currentTable.setLore(log)
            Persistence2.saveTable(currentTable)

caseManageTable = {'1' : caseAddC, '2' : caseDelC, '3' : caseAddP, '4' : caseDelP, '5' : caseOpen, '6' : caseClose, '7' : editLog}

#Character

def addCharacter(currentUser):
    name = Vision.entry("Character name: ")
    className = Vision.entry("Character Class: ")
    currentClass = Persistence2.getClass(className)
    char = Character(name, currentClass, currentUser)
    currentUser.addCharacter(currentUser, char)
    Persistence2.saveUser(currentUser)
    Persistence2.saveCharacter(char)

def delCharacter(currentUser):
    name = Vision.entry("Character name: ")
    char = currentUser.getCharacter(name)
    currentUser.delCharacter(currentUser, char)
    Persistence2.delCharacter(char)
    Persistence2.saveUser(currentUser)

def editCharacter(option, currentChar, currentUser, item):
    caseManageCharacter[option](currentChar, currentUser, item)

#Cases Manage Character

def caseUp(currentChar, currentUser, item):
    currentChar.gainLevel(currentUser)
    Persistence2.saveCharacter(currentChar)

def caseDown(currentChar, currentUser, item):
    currentChar.loseLevel(currentUser)
    Persistence2.saveCharacter(currentChar)

def caseGainXP(currentChar, currentUser, number):
    currentChar.addExperience(currentUser, int(number))
    Persistence2.saveCharacter(currentChar)

def caseLoseXp(currentChar, currentUser, number):
    currentChar.loseExperience(currentUser, int(number))
    Persistence2.saveCharacter(currentChar)

def caseAddInv(currentChar, currentUser, item):
    currentChar.addItem(currentUser, item)
    Persistence2.saveCharacter(currentChar)

def caseRemInv(currentChar, currentUser, item):
    currentChar.delItem(currentUser, item)
    Persistence2.saveCharacter(currentChar)

def caseShowInv(currentChar, currentUser, item):
    Inv = currentChar.getInventory()
    for it, index in enumerate(Inv):
        Vision.display(str(it) + ' - '+ index)

def caseDisplayChar(currentChar, currentUser, item):
    Vision.display('- Character Sheet: -')
    Vision.display('Name: '     + currentChar.getName())
    Vision.display('Owner: '    + currentChar.getCreator().getName())
    Vision.display('Class: '    + currentChar.getClass().getName())
    Vision.display('Level: '    + str(currentChar.getLevel()))
    Vision.display('Experience: ' + str(currentChar.getExperience()))
    Vision.display('--- Description: ---')
    Vision.display(currentChar.getDescription())
    Vision.display('---- Atributes: ----')
    attri = currentChar.getAtributes()
    for atribute in attri:
        Vision.display(atribute)
    Vision.display('---- Inventory: ----')
    caseShowInv(currentChar, currentUser, item)

def addUser(name, passw):
    Persistence2.saveUser(User(name, passw))

def displayCharacters(user):
    Vision.display('- Your Characters: -')
    chars = user.getCharacters()
    for char in chars:
        Vision.display(char.getName())



caseManageCharacter = {'0' : caseDisplayChar, '1' : caseUp, '2' : caseDown, '3' : caseGainXP, '4' : caseLoseXp, '5' : caseShowInv, '6' : caseAddInv, '7' : caseRemInv}
