import Control
import Vision
from User import User
from Class import Class
from Table import Table
from Character import Character
import Persistence
import sys

option = int(Vision.entry('1 - Login\n2 - Sign Up\n3 - Exit\n'))
if option == 1:
    name = Vision.entry('Login: ')
    password = Vision.entry('Password: ')
elif option == 2:
    name = Vision.entry('Login: ')
    password = Vision.entry('Password: ')
    confirmPassword = Vision.entry('Confirm Password: ')
    while password != confirmPassword:
        Vision.display('Invalid Password. Try again')
        password = Vision.entry('Password: ')
        confirmPassword = Vision.entry('Confirm Password: ')
else:
    sys.exit('')

currentUser = User(name, password)
currentClass = Class('wiz', currentUser)
currentChar = Character('nome', currentClass, currentUser)
currentTable = Table('mesa', currentUser)

Persistence.saveUser(currentUser)
Persistence.saveClass(currentClass)

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
                                 "6 - Close Table\n7 - Edit Logs\n8 - Change Table\n9 - Exit\n")
            if int(y) > 8:
                break
            if int(y) == 8:
                name = Vision.entry("Table name: ")
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
        if int(y) == 3 or int(y) == 4:
            item = Vision.entry('XP value: ')
        if int(y) == 6 or int(y) == 7:
            item = Vision.entry('Item name: ')
        Control.editCharacter(y, currentChar, currentUser, item)
    else:
        break
