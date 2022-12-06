inputfile = "puzzle1input.txt"
highest = 0
linesum = 0

with open(inputfile, 'r') as f:
    lines = f.readlines()

for line in lines:
    if line != '\n':
        linesum = linesum + int(line)
    if line == '\n':
        if linesum > highest:
            highest = linesum
        linesum = 0
      
print ("Highest sum is :" + str(highest))


    