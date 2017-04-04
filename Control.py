class Control:

    def addClass():
        name = input("Class name: ")
        FileManager.createFile(name)
        FileManager.createFile("\n")

    def addAbility():
        ability = input("Ability Description: ")
        FileManager.createFile(ability)
        FileManager.createFile("\n")

    def addColaborator():
        name = User.name
        FileManager.createFile(name)
        FileManager.createFile("\n")
