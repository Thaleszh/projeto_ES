import Control
import Vision

while True:
    x = int(Vision.entry("\n1 - Add Class\n2 - Search Class\n3 - Add Ability\n"+
                         "4 - Create Table\n5 - Create Character\n"+
                         "6 - Manage Table\n7 - Exit\n"))
    if x == 1:
        Control.addClass()
    elif x == 2:
        Control.searchTag()
    elif x == 3:
        Control.addAbility()
    elif x == 4:
        Control.createTable()
    elif x == 5:
        Control.createCharacter()
    elif x == 6:
        Control.editTable()
    else:
        break
