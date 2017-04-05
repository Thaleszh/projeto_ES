import Control
import Vision

while True:
    x = int(Vision.entry("\n1 - Add Class\n2 - Search Class\n3 - Add Ability\n4 - Exit\n"))
    if x == 1:
        Control.addClass()
    elif x == 2:
        Control.searchTag()
    elif x == 3:
        Control.addAbility()
    else:
        break
