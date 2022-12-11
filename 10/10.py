with open('./input.txt') as f:
    lines = [line.strip('\n') for line in f]

cycle = 0
register = 1
isAdding = 0
totalScore = 0
for cycle in range(1, 230):
    if (cycle + 20) % 40 == 0:
        print('ALERT!', cycle, register)
        totalScore += (cycle * register)
    if isAdding != 0:
        register += isAdding
        print(cycle, 'ADDING', isAdding, 'Register value: ', register)
        isAdding = 0
        continue
    if len(lines) == 0:
        print('EMPTY COMMAND LIST')
        break

    line = lines.pop(0)
    command = line.split(' ')
    # print(command)
    print(cycle, command, register)

    match command[0]:
        case 'noop':
            continue
        case 'addx':
            isAdding = int(command[1])

print(totalScore)
