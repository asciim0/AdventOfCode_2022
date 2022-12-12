# This solves Advent of Code Day 8 puzzle 2

input = 'input.txt'

score = 0
lineCount = 1
scenicScore = 0


def getColumn(position, file):
    f = open(file)
    fileLines = f.readlines()
    column = []
    for fileLine in fileLines:
        fileLine = fileLine.strip()
        fileLine = [*fileLine]
        column.append(fileLine[position])
    return column       

def checkRow(position, row):
    scenVert = 0
    scenVertA = 0
    scenVertB = 0
    left = row[0:(position)]
    left.reverse()
    right = row[(position+1):]
    tree = row[position]
    for elem in left:
        if int(elem) < int(tree):
            scenVertA = scenVertA + 1
        elif int(elem) == int(tree):
            scenVertA = scenVertA + 1
            break
        else:
            break
    for elem in right:
        if int(elem) < int(tree):
            scenVertB = scenVertB + 1
        else:
            scenVertB = scenVertB + 1
            break
    scenVert = scenVertA * scenVertB
    return scenVert

f = open(input)
lines = f.readlines()[1:-1]

for line in lines:
    line = line.strip()
    treerow = [*line]
    length = len(treerow)
    i = 1
    while i <= (length - 2):
        horizontalScore = checkRow(i, treerow)
        treeCol = getColumn(i, input)
        verticalScore = checkRow(lineCount, treeCol)
        total = int(horizontalScore) * int(verticalScore)
        if total > score:
            score = total
        i = i + 1
    lineCount = lineCount + 1

print ("Highest Scenic Score is: " + str(score))




