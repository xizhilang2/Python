from sys import argv
from os.path import exists

script, fromFile, toFile = argv

# print(f"Copying from {fromFile} to {toFile}")
#
# # we could do these two on one line, how?
# # inData = open(fromFile).read()
# inFile = open(fromFile)
# inData = inFile.read()
#
# print(f"The input file is {len(inData)} bytes long.")
#
# print(f"Does the output file exist? {exists(toFile)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()
#
# outFile = open(toFile, 'w')
# outFile.write(inData)
#
# print("Alright, all done.")
#
# outFile.close()
# inFile.close()

# all to one line:
open(toFile, 'w').write(open(fromFile).read())
