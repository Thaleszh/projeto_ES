class FileManager:

    def createFile(text):
        fi = open(text, "w+")
        fi.close

    def writeFile(text, name):
        fi = open(name, "w")
        fi = write(text)
        fi.close
