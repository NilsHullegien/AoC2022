with open('./input.txt') as f:
    lines = [line.strip('\n') for line in f]

register = 1
isAdding = 0
totalScore = 0
crt = []
currentCrt = []
for cycle in range(1, 241):
    if (cycle + 20) % 40 == 0:
        print('ALERT!', cycle, register)
        totalScore += (cycle * register)
        currentCrt.append(crt)
    if abs(register - ((cycle % 40)-1)) <= 1:
        print(cycle, 'register:', register, '#')
        crt.append('#')
    else:
        print(cycle, 'register:', register, '.')
        crt.append('.')
    if isAdding != 0:
        register += isAdding
        # print(cycle, 'ADDING', isAdding, 'Register value: ', register)
        isAdding = 0
        continue

    if len(lines) == 0:
        print('EMPTY COMMAND LIST')
        break

    line = lines.pop(0)
    command = line.split(' ')
    # print(command)
    # print(cycle, command, register)

    match command[0]:
        case 'noop':
            continue
        case 'addx':
            isAdding = int(command[1])

print('10a:', totalScore)
print('10b:')
print("".join(crt[:40]))
print("".join(crt[40:80]))
print("".join(crt[80:120]))
print("".join(crt[120:160]))
print("".join(crt[160:200]))
print("".join(crt[200:240]))
