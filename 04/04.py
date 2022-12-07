with open('04/input.txt') as f:
    lines = f.read().split('\n')




total = 0
for line in lines:
    elems = line.split(',')
    firstRangeNrs = [int(x) for x in elems[0].split('-')];
    secondRangeNrs = [int(x) for x in elems[1].split('-')];
    if (firstRangeNrs[0] <= secondRangeNrs[0] and firstRangeNrs[1] >= secondRangeNrs[1]) or (firstRangeNrs[0] >= secondRangeNrs[0] and firstRangeNrs[1] <= secondRangeNrs[1]):
        total += 1;
print('4a:', total)


## Partial contain
total = 0
for line in lines:
    elems = line.split(',')
    firstRangeNrs = elems[0].split('-');
    secondRangeNrs = elems[1].split('-');
    firstRange = range(int(firstRangeNrs[0]), int(firstRangeNrs[1]) + 1);
    secondRange = range(int(secondRangeNrs[0]), int(secondRangeNrs[1]) + 1);
    if set(firstRange) & set(secondRange):
        total += 1;
print('4b:', total)



