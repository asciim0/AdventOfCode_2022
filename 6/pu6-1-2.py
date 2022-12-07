# This solves Advent of Code Day 6 puzzles 1 and 2. Adjust seqLength variable accordingly

with open('input.txt', 'r') as file:
    data = file.read().rstrip()

# seqLength for puzzle 1 is 4, for puzzle 2 is 14
seqLength = 14
start = 0
inputLength = len(data)

while seqLength < inputLength:
    code = data[start:(start+seqLength)]
    
    # checks if characters in code are uniq
    x=list(set(code))
    y=list(code)
    x.sort()
    y.sort()
    if(x==y):
        print ("Code last char position at: " + str(start+seqLength))
        break
    
    start = start + 1
