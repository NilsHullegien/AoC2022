import math;
stacks = [];
moveOps = [];

with open('05/input.txt') as f:
    lines = [line.strip('\n') for line in f];
    baseLen = len([*lines[0]]);
    print(baseLen);
    for i in range(0, math.ceil(baseLen / 4)):
        stacks.append([]);
    print(stacks);
    for line in lines:
        if line.startswith(' 1') or line == '':
            continue;
        elif line.startswith('move'):
            moveLine = line.split(' ');
            moveLine.remove('move');
            moveLine.remove('from');
            moveLine.remove('to');
            print(moveLine);
            moveOps.append(
                {'amount': int(moveLine[0]), 'from': int(moveLine[1]) - 1, 'to': int(moveLine[2]) - 1}
            );
            continue;
        else:
            lineArr = [*line];
            for i in range(1, baseLen, 4) :
                print(i, lineArr[i]);
                if lineArr[i] != ' ':
                    stacks[math.floor(i / 4)].append(lineArr[i]);
for stack in stacks:
    stack.reverse();
print(stacks);
print(moveOps);

#5a: 
# while len(moveOps) > 0:
#     move = moveOps.pop(0);
#     print('NEW MOVE:', move);
#     for i in range(0, move['amount']):
#         item = stacks[move['from']].pop();
#         print('ITEM TO MOVE:', item);
#         stacks[move['to']].append(item);
#     print(stacks);
# print('FINAL', stacks);
# final = '';
# for stack in stacks:
#     final += stack[-1];
# print(final)

#5b: 
while len(moveOps) > 0:
    move = moveOps.pop(0);
    print('NEW MOVE:', move);
    items = []
    for i in range(0, move['amount']):
        items.append(stacks[move['from']].pop());
    print('items:', items);
    items.reverse()
    stacks[move['to']].extend(items);
    print(stacks);
print('FINAL', stacks);
final = '';
for stack in stacks:
    final += stack[-1];
print(final)