import FileManager

def addClass():
    name = input("Class name: ")
    FileManager.createFile(name)
    ability = input("Ability Description: ")
    FileManager.writeFile(ability + "\n", name)

def addAbility():
    name = input("Class name: ")
    ability = input("Ability Description: ")
    FileManager.writeFile(ability+"\n", name)

def addColaborator():
    usr = User.name
    FileManager.writeFile(name+"\n", name)

def searchTag():
    name = input("Class name: ")
    FileManager.readFile(name)

def changeName():
    old = input("Class name: ")
    new = input("New Class Name: ")
    FileManager.renameFile(old, new)
