import pandas as pd

df = pd.read_csv('rps2.txt', delim_whitespace=True)

def calcInput(row):
    if row['outcome'] == "draw":
        return row['elf']
    elif row['outcome'] == "win" and row['elf'] == "Paper":
        return "Scissors"
    elif row['outcome'] == "win" and row['elf'] == "Rock":
        return "Paper"
    elif row['outcome'] == "win" and row['elf'] == "Scissors":
        return "Rock"
    elif row['outcome'] == "lose" and row['elf'] == "Paper":
        return "Rock"
    elif row['outcome'] == "lose" and row['elf'] == "Rock":
        return "Scissors"
    elif row['outcome'] == "lose" and row['elf'] == "Scissors":
        return "Paper"

def assignPoints(row):
    if row['me'] == "Rock":
        return 1
    elif row['me'] == "Paper":
        return 2
    elif row['me'] == "Scissors":
        return 3
    return 0

def assignRoundPoints(row):
    if row['outcome'] == "lose":
        return 0
    elif row['outcome'] == "draw":
        return 3
    elif row['outcome'] == "win":
        return 6

def calcuateScore(row):
    roundscore = int(row['points']) + int(row['result'])
    return roundscore
    

df['elf'] = df['elf'].map({'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'})
df['outcome'] = df['outcome'].map({'X': 'lose', 'Y': 'draw', 'Z': 'win'})
df['me'] = df.apply(lambda row: calcInput(row), axis=1)
df['points'] = df.apply(lambda row: assignPoints(row), axis=1)
df['result'] = df.apply(lambda row: assignRoundPoints(row), axis=1)
df['score'] = df.apply(lambda row: calcuateScore(row), axis=1)
totalScore = df['score'].sum()

print ("The total score is: " + str(totalScore))
