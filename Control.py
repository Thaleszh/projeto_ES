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
