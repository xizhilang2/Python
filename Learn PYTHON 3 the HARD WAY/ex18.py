# this one is like your scripts with argv
def printThree(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

# ok, that *args is actually pointless, we can just do this
def printTwoAgain(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just tkes one argument
def printOne(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def printNone():
    print("I got nothin'.")

printThree("Zed","Shaw","Erica")
printTwoAgain("Zed","Shaw")
printOne("First!")
printNone()
