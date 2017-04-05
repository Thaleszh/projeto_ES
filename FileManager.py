import os
import shutil

def createFile(text):
    fi = open(text + ".txt", "w+")
    fi.close

def writeFile(text, name):
    fi = open(name + ".txt", "a")
    fi.write(text)
    fi.close

def readFile(name):
    fi = open(name + ".txt", "r")
    for line in fi:
        print(line, end='')
    fi.close

def renameFile(old, new):
    os.rename(old + ".txt", new + ".txt")

def copyFile(old, new):
    shutil.copy2(old + ".txt", new + ".txt")

def removeFile(name):
    os.remove(name + ".txt")
