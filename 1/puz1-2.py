inputfile = "puzzle1input.txt"
linesum = 0
allSums = []

with open(inputfile, 'r') as f:
    lines = f.readlines()

for line in lines:
    if line != '\n':
        linesum = linesum + int(line)
    if line == '\n':
        allSums.append(linesum)
        linesum = 0
        
allSums.sort(reverse=True)
ergebnis = sum(allSums[0:3])
print ("Sum of 3 highest is: " + str(ergebnis))


    