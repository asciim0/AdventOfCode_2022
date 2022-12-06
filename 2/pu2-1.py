import pandas as pd

inputfile = "rps.txt"
df = pd.read_csv('rps.txt', delim_whitespace=True)
totalScore = 0

def assignPoints(row):
    if row['me'] == "Rock":
        return 1
    elif row['me'] == "Paper":
        return 2
    elif row['me'] == "Scissors":
        return 3
    return 0

def calculateWin(row):
    if ((row['elf'] == "Rock" and row['me'] == "Paper") or (row['elf'] == "Paper" and row['me'] == "Scissors") or (row['elf'] == "Scissors" and row['me'] == "Rock")):
        # this is a win!
        return 6
    elif (row['elf'] == "Rock" and row['me'] == "Rock") or (row['elf'] == "Paper" and row['me'] == "Paper") or (row['elf'] == "Scissors" and row['me'] == "Scissors"):
        # this is a draw!
        return 3
    return 0

def calcuateScore(row):
    roundscore = int(row['points']) + int(row['result'])
    return roundscore
    
df['elf'] = df['elf'].map({'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'})
df['me'] = df['me'].map({'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'})
df['points'] = df.apply(lambda row: assignPoints(row), axis=1)
df['result'] = df.apply(lambda row: calculateWin(row), axis=1)
df['score'] = df.apply(lambda row: calcuateScore(row), axis=1)
totalScore = df['score'].sum()

print ("The total score is: " + str(totalScore))



