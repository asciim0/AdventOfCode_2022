# This solves Advent of Code Day 7 puzzles 1 and 2. Adjust seqLength variable accordingly

input = 'input.txt'

maxSize = 100000
currentDir = "/"
fileListDict = {}
dirSizeDict = {}
dirDict = {}
usedSpace = 0

def updateDir(dictKey, addSize, d):
    if dictKey in d:
        oldsize = int(d[dictKey])
        newsize = oldsize + addSize
        updateDict = {dictKey:newsize} 
    else:
        updateDict = {dictKey:fileSize}
    return updateDict

# reads file and interpretes lines, sets currentDictionary 
for line in open(input, encoding="utf-8"):
    currentLine = ((line.strip()).split(" "))
    if currentLine[0] == "$" and currentLine[1] == "cd":
        if currentLine[2] != "..":
            currentDir = currentDir + "/" + currentLine[2]
            while currentDir.startswith("//"):
                currentDir = currentDir[1:]
        else:
            currentDir = currentDir.rsplit("/", 1)[0]
            while currentDir.startswith("//"):
                currentDir = currentDir[1:]

# for files, reads path and adds filesize in dictionary for all breadcrumbs, if path already exists entry is updated 
    elif currentLine[0].isdigit():
        pathlength = len(currentDir.split("/"))-1
        i = 1
        fileSize = int(currentLine[0])
        usedSpace = usedSpace + fileSize
        dirDict.update(updateDir(currentDir, fileSize, dirDict))
                
        while i < int(pathlength):
            resultDir = currentDir.rsplit("/", i)[0]
            i = i + 1
            dirDict.update(updateDir(resultDir, fileSize, dirDict))
  
# filters directory by maxsize and prints out answer to puzzle1    
resultDict = {k:v for (k,v) in dirDict.items() if v <= maxSize}
print ("Total size of directories smaller than " + str(maxSize) + " is " + str(sum(resultDict.values())))

# print directories
print ("Used Space is: " + str(usedSpace))
print ("Free Space is: " + str(70000000 - usedSpace))
toDelete = (30000000 - (70000000 - usedSpace))
print ("Space to be freed: " + str(toDelete))

result2Dict = {k:v for (k,v) in dirDict.items() if v >= toDelete}
sorted2Dict = {k: v for k, v in sorted(result2Dict.items(), key=lambda item: item[1])}

print (result2Dict)
print (sorted2Dict)

print ("The size of the smallest dict to be deleted is: " + str(list(sorted2Dict.values())[0]))




        

    