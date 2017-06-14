import Control
import Vision
import Persistence2
import sys
import Saves
from Class import Class
from Table import Table
from User import User
from Character import Character

Saves.addUsers()

#entry options
while(True):
    option = int(Vision.entry('1 - Login\n2 - Sign Up\n3 - Exit\n'))

    #login
    if option == 1:
        name = Vision.entry('Login: ')
        tempUser = Persistence2.getUser(name)
        # if user not found
        if type(tempUser) is not User:
            sys.exit('User Not Found')
        else:
            password = Vision.entry('Password: ')
            # set number of extra tries
            tries = 3
            # while password is not right
            while password != tempUser.getPassword() and tries > 0:
                Vision.display('Wrong password. ' + str(tries) + ' tries remaining')
                password = Vision.entry('Password: ')
                tries -= 1
            if tries <= 0:
                sys.exit('Out of Tries')
    # new user
    elif option == 2:
        name = Vision.entry('Login: ')
        password = Vision.entry('Password: ')
        confirmPassword = Vision.entry('Confirm Password: ')
        while password != confirmPassword:
            Vision.display('Invalid Password. Try again')
            password = Vision.entry('Password: ')
            confirmPassword = Vision.entry('Confirm Password: ')
        currentUser = User(name, password)
        Persistence2.saveUser(currentUser)  

    # exit  
    else:
        sys.exit('Goodbye')

    currentUser = User(name, password)
    Persistence2.saveUser(currentUser)
    Saves.addClasses(currentUser)
    Saves.addCharacters(currentUser)
    Saves.addTables()

    currentClass = Class('wiz', currentUser)
    currentChar = Character('nome', currentClass, currentUser)
    currentTable = Table('mesa', currentUser)
    item = ''

    Persistence2.saveClass(currentClass)

    while True:
        x = int(Vision.entry("\n1 - Add Class\n2 - Search Class\n3 - Add Ability\n"+
                             "4 - Create Table\n5 - Manage Table\n"+
                             "6 - Create Character\n7 - Manage Character\n8 - Display Characters\n9 - Logout\n10 - Exit\n"))
        if x == 1:
            Control.addClass(currentUser)
        elif x == 2:
            Control.searchClass(Vision.entry("Class name: "))
        elif x == 3:
            Control.addAbility(currentClass)
        elif x == 4:
            Control.createTable(currentUser)
        elif x == 5:
            name = Vision.entry('Table name: ')
            currentTable = Persistence2.getTable(name)
            while True:
                y = Vision.entry("\n1 - Add Character\n2 - Remove Character\n"+
                                     "3 - Add PLayer\n4 - Remove Player\n5 - Open Table\n"+
                                     "6 - Close Table\n7 - Edit Logs\n8 - Change Table\n9 - Exit\n")
                if int(y) > 8:
                    break
                if int(y) == 8:
                    name = Vision.entry("Table name: ")
                    currentTable = Persistence2.getTable(name)
                else:
                    Control.editTable(y, currentTable)
        elif x == 6:
            Control.addCharacter(currentUser)
        elif x == 7:
            name = Vision.entry('Character Name: ')
            currentChar = Persistence2.getCharacter(name)
            while(True):
                y = Vision.entry("\n0 - Display Character info\n1 - Up Character\n2 - Down Character\n"+
                                     "3 - Add XP\n4 - Remove XP\n5 - Show Inventory\n"+
                                     "6 - Add to Inventory\n7 - Remove from Inventory\n8 - Exit\n")
                if int(y) > 7:
                    break
                elif int(y) == 3 or int(y) == 4:
                    item = Vision.entry('XP value: ')
                elif int(y) == 6 or int(y) == 7:
                    item = Vision.entry('Item name: ')
                Control.editCharacter(y, currentChar, currentUser, item)
        elif x == 8:
            Control.displayCharacters(currentUser)
        elif x == 9:
            break
        else:
            sys.exit('Goodbye')
