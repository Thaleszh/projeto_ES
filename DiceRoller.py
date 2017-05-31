import Vision
from random import randint
class DiceRoller:

     def roll(self, sides, quantity):
         result = list()
        for x in quantity:
            result.append(randint(1,sides))
        return result
