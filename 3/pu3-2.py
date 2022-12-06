import string
from itertools import zip_longest

inputfile = 'packlist.txt'
totalScore = 0

def compareStrings (elements):
    i = 0
    str1 = elements[0]
    str2 = elements[1]
    str3 = elements[2]
    for c in str1:
        char = str1[i]
        if char in str2:
            if char in str3:
                return char
        i = i + 1
    return 0

def calcuateScore (duplicate):
    lowerC = dict(zip(string.ascii_lowercase, range(1,27)))
    upperC = dict(zip(string.ascii_uppercase, range(27,53)))
    if duplicate in lowerC.keys():
        return lowerC.get(duplicate)
    elif duplicate in upperC.keys():
        return upperC.get(duplicate)

with open(inputfile) as f:
    for next_n_lines in zip_longest(*[f] * 3):
        multLines = [x[:-1] for x in list(next_n_lines)]
        duplicatez = compareStrings(multLines)
        priority = calcuateScore(duplicatez)
        totalScore = totalScore + priority
        
print ("Total sum of priorities is: " + str(totalScore))
    
    


    