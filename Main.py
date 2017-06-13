import Control
import Vision
from User import User
from Class import Class
from Table import Table
from Character import Character
import Persistence

currentUser = User('user', 'guest')
currentClass = Class('wiz', currentUser)
currentChar = Character('nome', currentClass, currentUser)
currentTable = Table('mesa', currentUser)

Persistence.saveClass(currentClass)
Persistence.saveUser(currentUser)

while True:
    x = int(Vision.entry("\n1 - Add Class\n2 - Search Class\n3 - Add Ability\n"+
                         "4 - Create Table\n5 - Manage Table\n"+
                         "6 - Create Character\n7 - Manage Character\n8 - Exit\n"))
    if x == 1:
        Control.addClass(currentUser)
    elif x == 2:
        Control.searchTag()
    elif x == 3:
        Control.addAbility(currentClass)
    elif x == 4:
        Control.createTable(currentUser)
    elif x == 5:
        name = Vision.entry('Table name: ')
        currentTable = Persistence.getTable(name)
        while True:
            y = Vision.entry("\n1 - Add Character\n2 - Remove Character\n"+
                                 "3 - Add PLayer\n4 - Remove Player\n5 - Open Table\n"+
                                 "6 - Close Table\n7 - Edit Logs\n8 - Change Table\n9- Exit\n")
            if int(y) > 8:
                break
            if int(y) == 8:
                currentTable = Persistence.getTable(name)
            else:
                Control.editTable(y, currentTable)
    elif x == 6:
        Control.addCharacter(currentUser)
    elif x == 7:
        name = Vision.entry('Character Name: ')
        currentChar = Persistence.getCharacter(name)
        y = Vision.entry("\n1 - Up Character\n2 - Down Character\n"+
                             "3 - Add XP\n4 - Remove XP\n5 - Show Inventory\n"+
                             "6 - Add to Inventory\n7 - Remove from Inventory\n8 - Exit\n")
        if int(y) > 7:
            break
        Control.editCharacter(y, currentChar, currentUser)
    else:
        break
