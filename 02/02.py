with open('02/input.txt') as f:
    lines = [line.rstrip().split(' ') for line in f];

scoreMap = {
    'X': 1, #R
    'Y': 2, #P
    'Z': 3  #S
}

opponentMap = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

resultScoreMap = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

fullScoreMap = {
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7,
}

#2a:
totalScore = 0;
for line in lines:
    opponent = line[0];
    self = line[1];
    selfScore = scoreMap[self]
    opponentScore = scoreMap[opponentMap[opponent]];
    totalScoreForRound = selfScore;
    if (selfScore == opponentScore):
        totalScoreForRound += 3;
    
    if ((selfScore == 1 and opponentScore == 3) or (selfScore == 2 and opponentScore == 1) or (selfScore == 3 and opponentScore == 2)):
        totalScoreForRound += 6;
    totalScore += totalScoreForRound;
    

print('2a:', totalScore);

#2b:
totalScore = 0;
for line in lines:
    totalScore += fullScoreMap[''.join(line)];
    

print('2b:', totalScore);







