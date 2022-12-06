# This solves Advent of Code puzzles 1 and 2, see variable puzzleNo

instruction = 'instruct.txt'
initial = 'initial.txt'

# indicate whether solving puzzle 1 or 2 - depending on this the moved boxes order will be determined
puzzleNo = 1

stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack9, stack8 = ([] for _ in range(9))

def stripEmpty(stack):
    # this removes the first element (was stack number), all whitespaces and empty elements for each stack
    stack = [ele for ele in stack if ele.strip()]
    stack = list(map(str.strip, stack))
    del stack[0]
    return stack

def splitInstructions(instr):
    # splits instructions into dictionary
    instr = instr.strip()
    instr = instr.replace("move ", "move:")
    instr = instr.replace("from ", "from:")
    instr = instr.replace("to ", "to:")    
    res = dict(map(str.strip, sub.split(':', 1))
           for sub in instr.split(' ') if ':' in sub)
    return res

for line in reversed(list(open(initial))):
    #this is a very unsophisticated way of reading the positions into different lists
    stack1.append(line[:4])
    stack2.append(line[4:8])
    stack3.append(line[8:12])
    stack4.append(line[12:16])
    stack5.append(line[16:20])
    stack6.append(line[20:24])
    stack7.append(line[24:28])
    stack8.append(line[28:32])
    stack9.append(line[32:35])

i = 1
while i < 10:
    globals()["stack" + (str(i))] = stripEmpty(globals()["stack" + (str(i))])
    i = i + 1

with open(instruction, 'r') as f2:
    lines2 = f2.readlines()

for line2 in lines2:
    instruction = (splitInstructions(line2))

    # Anz is the number of boxes that are moved (added "-" for the index location)
    # switch is a new list with the boxes currently on the crane
    anz = "-" + instruction['move']
    from_stack = (globals()["stack" + (str(instruction['from']))])
    to_stack = (globals()["stack" + (str(instruction['to']))])
    switch = (from_stack[int(anz):])

    del (from_stack[int(anz) :])
    if puzzleNo == 2:
        switch.reverse()
    to_stack.extend(switch)
    
answer = []
answer = stack1[-1:] + stack2[-1:] + stack3[-1:] + stack4[-1:] + stack5[-1:] + stack6[-1:] + stack7[-1:] + stack8[-1:] + stack9[-1:]

print ("The answer is: ")
print ((''.join(str(e) for e in answer)).translate({ord(c):'' for c in '[]'}))