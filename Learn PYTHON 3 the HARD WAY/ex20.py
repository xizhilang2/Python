from sys import argv

script, inputFile = argv

def printAll(fileInput):
    print(fileInput.read())

def rewind(fileInput):
    fileInput.seek(0)

def printALine(lineCount, f):
    print(f"This's {lineCount} line:", f.readline(), end="")

currentFile = open(inputFile)

print("First let's print the whole file:\n")

printAll(currentFile)

print("Now let's rewind, kind of like a tape.")

rewind(currentFile)

print("Let's prit three lines:")

currentLine = 1
printALine(currentLine, currentFile)

currentLine += 1
printALine(currentLine, currentFile)

currentLine += 1
printALine(currentLine, currentFile)
