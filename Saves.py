import Control
import Vision
import Persistence
import sys
from Class import Class
from Table import Table
from User import User
from Character import Character


def addUsers():
    Control.addUser('Toni', 'toni')
    Control.addUser('Rafael', 'guest')
    Control.addUser('Thales', 'thales')
    Control.addUser('Vania', 'tranquilo')
    Control.addUser('Stark', '123')
    Control.addUser('Vina', 'rainbow6')
    Control.addUser('Luis', 'morte')

def addClasses(user):
    tempClass = Class('Wizard', user)
    tempClass.addAbility('Arcane Usage', 'The wizard is proficient in casting spells. He has access to a grimoire that he can compose')
    tempClass.addAbility('Bolt', 'The wizard can charge a bolt of a chosen element at will, channeling a bit of his mana')
    Persistence.saveClass(tempClass)

    tempClass = Class('Rogue', user)
    tempClass.addAbility('Stealth', 'The rogue can walk silently and hide easily, he is overall sneaky.')
    tempClass.addAbility('Sneak Attack', 'As a rogue can strike from the shadows with extra damage, or seize moments of opportunity')
    Persistence.saveClass(tempClass)

def addCharacters(user):
    clas = Persistence.getClass('Rogue')
    tempChar = Character('Artemis Entreri', clas, user)
    inventory = list()
    inventory.append('Dagger')
    inventory.append('Cloak')
    inventory.append('Short Sword')
    tempChar.setInventory(user, inventory)
    user.addCharacter(user, tempChar)
    Persistence.saveUser(user)
    Persistence.saveCharacter(tempChar)


def addTables():
    pass
