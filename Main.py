import Control
import Vision

while True:
    x = int(Vision.entry("\n1 - Add Class\n2 - Search Class\n3 - Edit Class\n4 - Remove Class\n5 - Exit\n"))
    if x == 1:
        Control.addClass()
    elif x == 2:
        Control.searchTag()
    elif x == 3:
        y = int(Vision.entry("  1 - Add Ability\n  2 - Change Class Name\n  3 - Duplicate Class\n"))
        if y == 1:
            Control.addAbility()
        elif y == 2:
            Control.changeName()
        else:
            Control.duplicateClass()
    elif x == 4:
        Control.removeCLass()
    else:
        break
