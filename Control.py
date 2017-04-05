from Class import Class
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
    abilityName = Vision.entry("Ability name: ")
    abilityDescription = Vision.entry("Ability Description: ")
    tempClass.addAbility(user, abilityName, abilityDescription)
    Persistencia.saveClass(tempClass)

def addColaborator():
    usr = User.name
    FileManager.writeFile(name+"\n", name)

def searchTag():
    name = Vision.entry("Class name: ")
    classe = Persistencia.getClass(name)
    displayClass(classe)

def displayClass(classe):
	Vision.display("\nClasse - " + classe.getName() + ": \n--------------\nAbilites:")
	for ability in classe.getAbilities():
		Vision.display(ability.getName()+": " + ability.getDescription())

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
