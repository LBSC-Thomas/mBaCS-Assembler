'''This is LBSC's assembler for Swift's mBaCS
   Disclaimer: I don't own the instruction set, all the rights go to Swift.
'''
import sys
getInputFile = input("Please type in the directory of the file you'd like to assemble: ")

if ".mbacs" in getInputFile:
    openInputFile = open(getInputFile, "r")
    readInputFile = openInputFile.read()
    loadInputFile = str(readInputFile)
    if loadInputFile != None:
        fetchOutputFile = getInputFile.replace(".mbacs",".out")
        outputFile = open(fetchOutputFile, "w+")
        mBacsTokens = {"ADD": "000",
                       "SUB": "001",
                       "FC": "010",
                       "!A": "011",
                       "!B": "100",
                       "FB": "101",
                       "LIM": "110"}
        mBacsValues = {"0": "000",
                       "1": "001",
                       "2": "010",
                       "3": "011",
                       "4": "100",
                       "5": "101",
                       "6": "110",
                       "7": "111"}

        tempProgram = loadInputFile.split()
        opcodeField = ""
        targetField = ""
        tempIndex = 0
        for line in tempProgram:
            if "@" in line:
                tempIndex += 1
                continue
            elif line in mBacsTokens:
                if "$" in tempProgram[tempIndex + 1]:
                    tempValue = tempProgram[tempIndex + 1]
                    tempTarget = tempValue.replace("$", "")
                    targetField = mBacsValues[tempTarget]
                    opcodeField = "101"
                    tempIndex += 1
                else:
                    targetField = "000"
                    opcodeField = mBacsTokens[line]
                    tempIndex += 1
            else:
                tempIndex += 1
                continue
            outputFile.write(opcodeField + targetField + "\n")
        opcodeField = ""
        targetField = ""
    else:
        print("Error: write a program.")
        sys.exit()

else:
    print("Error: please import a file with a valid extension (.mbacs)")
    sys.exit()