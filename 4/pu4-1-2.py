# This solves Advent of Code 2022 Day 4 Puzzles 1 and 2

inputfile = 'sectors.txt'
fullOverlap = 0
fullSubContain = 0
partOverlap = 0

def splitPairs(pair):
    elf1, elf2 = pair.split(',')
    elf1_min, elf1_max = elf1.split('-')
    elf2_min, elf2_max = elf2.split('-')
    elf1_sectors = list(range(int(elf1_min), int(elf1_max)+1))
    elf2_sectors = list(range(int(elf2_min), int(elf2_max)+1))
    return elf1_sectors, elf2_sectors

def checkSubOverlap(range1, range2):
    return (all(elem in range1 for elem in range2) or all(elem in range2 for elem in range1))

def checkPartOverlap(range1, range2):
    return (any(elem in range1 for elem in range2) or all(elem in range2 for elem in range1))

with open(inputfile) as f:
    for line in f:
        sec1, sec2 = splitPairs(line)
        if sec1 == sec2:
            fullOverlap = fullOverlap + 1
        if (checkSubOverlap(sec1, sec2)):
            fullSubContain = fullSubContain + 1
        if (checkPartOverlap(sec1, sec2)):
            partOverlap = partOverlap + 1

print ("Number of full sector overlaps: " + str(fullOverlap))
print ("Number of full sector set subcontained in other sector set: " + str(fullSubContain))
print ("Number of partial sector overlaps: " + str(partOverlap))