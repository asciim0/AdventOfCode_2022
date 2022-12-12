# This solves Advent of Code Day 8 puzzle 1

input = 'input.txt'

score = 0
lineCount = 1

def getGridSize(inputfile):
    x = 0
    y = 0
    for line in open(inputfile):
        x = (len(line.strip()))
        y = y + 1
    return (x, y)

def getColumn(position, file):
    f = open(file)
    fileLines = f.readlines()
    column = []
    for fileLine in fileLines:
        fileLine = fileLine.strip()
        fileLine = [*fileLine]
        #print (fileLine)
        #print ("i will add position " + (str(position + 1)) + " which is " + str(fileLine[position]))
        column.append(fileLine[position])
    #print (column)
    return column       

def checkRow(position, row):
    left = row[0:(position)]
    right = row[(position+1):]
    tree = row[position]
    # print ("Tree: " + tree)
    #print ("left: " + str(left))
    #print ("right: " + str(right))
    if int(tree) > int(max(left)):
        #print ("zählt")
        return True
    elif int(tree) > int(max(right)):
        #print ("zählt")
        return True
    else:
        #print ("zero points")
        return False 

f = open(input)
lines = f.readlines()[1:-1]
#lines = f.readlines()
for line in lines:
    line = line.strip()
    treerow = [*line]
    length = len(treerow)
    #print (treerow)
    #print (len(treerow))
    # i is position of char in line (relevant for check row), x is position of line in input (relevant for check column)
    i = 1
    while i <= (length - 2):
        if checkRow(i, treerow):
            #print ("win")
            score = score + 1
        else:
            treeCol = getColumn(i, input)
            #print("Column: " + str(treeCol))
            if checkRow(lineCount, treeCol):
                #print ("x :" + str(x))
                #print ("win")
                score = score + 1
        i = i + 1
    lineCount = lineCount + 1
# get dimensions and add border trees to treecount
length, height = getGridSize(input)
treeCount = 2*length + 2*height - 4
treeCount = treeCount + score
print ("Amount of visible trees: " + str(treeCount))
