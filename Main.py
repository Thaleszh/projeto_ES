import Control
while True:
    x = int(input("\n1 - Add Class\n2 - Search Class\n3 - Edit Class\n4 - Exit\n"))
    if x == 1:
        Control.addClass()
    elif x == 2:
        Control.searchTag()
    elif x == 3:
        y = int(input("  1 - Add Ability\n  2 - Change Class Name\n"))
        if y == 1:
            Control.addAbility()
        else:
            Control.changeName()
    elif x == 4:
        break
