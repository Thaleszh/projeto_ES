import FileManager
import Vision

def addClass():
    name = Vision.entry("Class name: ")
    FileManager.createFile(name)
    ability = Vision.entry("Ability Description: ")
    FileManager.writeFile(ability + "\n", name)

def addAbility():
    name = Vision.entry("Class name: ")
    ability = Vision.entry("Ability Description: ")
    FileManager.writeFile(ability+"\n", name)

def addColaborator():
    usr = User.name
    FileManager.writeFile(name+"\n", name)

def searchTag():
    name = Vision.entry("Class name: ")
    FileManager.readFile(name)

def changeName():
    old = Vision.entry("Class name: ")
    new = Vision.entry("New Class Name: ")
    FileManager.renameFile(old, new)

def duplicateClass():
    old = Vision.entry("Class name: ")
    new = Vision.entry("New Class Name: ")
    FileManager.copyFile(old, new)

def removeCLass():
    name = Vision.entry("Class name: ")
    FileManager.removeFile(name)
