import string;

with open('03/input.txt') as f:
    lines = [line.rstrip() for line in f];
    
lowerCaseAlphabet=string.ascii_lowercase
upperCaseAlphabet=string.ascii_uppercase
    
#3a:
total = 0;
for line in lines:
    middle = int(len(line) / 2);
    firstHalf = set([*line[:middle]]);
    secondHalf = set([*line[middle:]]);
    common = firstHalf.intersection(secondHalf).pop();
    ordinal = lowerCaseAlphabet.find(common) + 1;
    if (ordinal == 0):
        ordinal = upperCaseAlphabet.find(common) + 27;
    total += ordinal;
print('3a:', total);

#3b: 
total = 0;
for i, j, k in zip(lines[0::3], lines[1::3], lines[2::3]):
    print(i,j,k);
    common = set([*i]).intersection(set([*j])).intersection(set([*k])).pop();
    ordinal = lowerCaseAlphabet.find(common) + 1;
    if (ordinal == 0):
        ordinal = upperCaseAlphabet.find(common) + 27;
    total +=  ordinal;
print('3b:', total);