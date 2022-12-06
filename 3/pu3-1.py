import string
inputfile = 'packlist.txt'
totalScore = 0

def compareStrings (string1, string2):
    i = 0
    for char in string1:
        char = string1[i]
        if char in string2:
            return char
        i = i + 1
    return 

def calcuateScore (duplicate):
    lowerC = dict(zip(string.ascii_lowercase, range(1,27)))
    upperC = dict(zip(string.ascii_uppercase, range(27,53)))
    if duplicate in lowerC.keys():
        return lowerC.get(duplicate)
    elif duplicate in upperC.keys():
        return upperC.get(duplicate)

with open(inputfile, 'r') as f:
    lines = f.readlines()

for line in lines:
    x = int((len(line)-1)/2)
    str1 = line[0:x]
    str2 = line[x:x*2]
    duplicates = compareStrings(str1, str2)
    priority = calcuateScore(duplicates)
    totalScore = totalScore + priority
    
print ("The sum of priorities for the item types is: " + str(totalScore))
    


    