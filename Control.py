from Class import Class
from Table import Table
from User import User
from Character import Character

import Vision
import Persistence

user = User('user', 'guest')
clas = Class('wiz', user)
Persistence.saveClass(clas)
Persistence.saveUser(user)

def addClass():
    name = Vision.entry("Class name: ")
    newClass = Class(name, user)
    Persistence.saveClass(newClass)

def addAbility():
    name = Vision.entry("Class name: ")
    tempClass = Persistence.getClass(name)
    keep = 1
    while (keep == 1):
        abilityName = Vision.entry("Ability name: ")
        abilityDescription = Vision.entry("Ability Description: ")
        tempClass.addAbility(user, abilityName, abilityDescription)
        keep = int(Vision.entry("Do you wish to keep adding abilities?\n 1- Yes \n 2- No\n"))
    Persistence.saveClass(tempClass)

def addColaborator():
    name = Vision.entry("Class name: ")
    classe = Persistence.getClass(name)

def searchTag():
    name = Vision.entry("Class name: ")
    classe = Persistence.getClass(name)
    displayClass(classe)

def displayClass(classe):
	Vision.display("\nClasse - " + classe.getName() + ": \n--------------\nAbilites:")
	for ability in classe.getAbilities():
		Vision.display(ability.getName()+": " + ability.getDescription())

def changeName():
    old = Vision.entry("Class to change name: ")
    new = Vision.entry("New Class Name: ")
    classe = Persistence.getClass(old)
    Persistence.delClass(classe)
    classe.setName(new)
    Persistence.saveClass(classe)

def duplicateClass():
    old = Vision.entry("Name of the class to duplicate: ")
    new = Vision.entry("New Class Name: ")
    classe = Persistence.getClass(old)
    classe.setName(new)
    Persistence.saveClass(classe)

def delClass():
    classe = Vision.entry("Name of the class to be deleted: ")
    Persistence.delClass(classe)

#Table
def createTable():
    name = Vision.entry("Table name: ")
    newTable = Table(name, user)
    Persistence.saveTable(newTable)

def delTable():
    name = Vision.entry("Table name: ")
    Persistence.delTable(name)

def editTable(option):
    cases[option]()

# cases Manage Table
def caseAddC():
    name = Vision.entry("Table name: ")
    table = Persistence.getTable(name)
    playerName = Vision.entry("Player name: ")
    player = Persistence.getUser(playerName)
    charName = Vision.entry("Character name: ")
    char = player.getCharacter(charName)
    table.addCharacter(user, char)
    Persistence.saveTable(table)

def caseDelC():
    name = Vision.entry("Table name: ")
    table = Persistence.getTable(name)
    playerName = Vision.entry("Player name: ")
    player = Persistence.getUser(playerName)
    charName = Vision.entry("Character name: ")
    char = player.getCharacter(charName)
    table.delCharacter(user, char)
    Persistence.saveTable(table)

def caseAddP():
    name = Vision.entry("Table name: ")
    table = Persistence.getTable(name)
    playerName = Vision.entry("Player name: ")
    player = Persistence.getUser(playerName)
    table.addPlayer(user, player)
    Persistence.saveTable(table)

def caseDelP():
    name = Vision.entry("Table name: ")
    table = Persistence.getTable(name)
    playerName = Vision.entry("Player name: ")
    player = Persistence.getUser(playerName)
    table.delPlayer(user, player)
    Persistence.saveTable(table)

def caseOpen():
    name = Vision.entry("Table name: ")
    table = Persistence.getTable(name)
    Persistence.addOpenTable(table)

def caseClose():
    name = Vision.entry("Table name: ")
    Persistence.delOpenTable(name)

def caseQuit():
    name = Vision.entry("Table name: ")
    table = Persistence.getTable(name)
    table.quit(player)

cases = {'1' : caseAddC, '2' : caseDelC, '3' : caseAddP, '4' : caseDelP, '5' : caseOpen, '6' : caseClose}

#Logs

def editLog():
    name = Vision.entry("Table name: ")
    table = Persistence.getTable(name)
    option = Vision.entry("\n1 - Edit Lore\n2 - Edit Log\n")
    if option == 1:
        lore = table.getLore()
        Vision.display(lore)
        lore = Vision.entry("Type the new lore: ")
        table.setLore(lore)
        Persistence.saveTable(table)
    else:
        log = table.getLog()
        Vision.display(log)
        log = Vision.entry("Type the new log: ")
        table.setLore(log)
        Persistence.saveTable(table)

#Character

def addCharacter():
    name = Vision.entry("Character name: ")
    className = Vision.entry("Character class: ")
    clas = Persistence.getClass(className)
    char = Character(name, clas, user)
    user.addCharacter(user, char)
    Persistence.saveUser(user)
    Persistence.saveCharacter(char)

def delCharacter():
    name = Vision.entry("Character name: ")
    char = user.getCharacter(name)
    user.delCharacter(user, char)
    Persistence.delCharacter(char)
    Persistence.saveUser(user)

#Cases Manage Character

def caseUp():
    Character.gainLevel(user)

def caseDown():
    Character.loseLevel(user)

def caseGainXP(user, number):
    Character.addExperience(number)

def caseLoseXp(user, number):
    Character.loseExperience(number)

def caseAddInv(item):
    Character.addItem(user, item)

def caseRemInv(item):
    Character.delItem(user, item)

def caseShowInv():
    Character.getInventory()
