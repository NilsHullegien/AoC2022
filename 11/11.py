from math import floor, prod


def parse(unparsedMonkeyList):
    res = []
    maxValue = 1
    for unparsedMonkey in unparsedMonkeyList:
        startingItems = [int(x) for x in unparsedMonkey[1].split(':')[1].split(',')]
        operation = parseOperation(unparsedMonkey[2].split('=')[1].strip(' '))
        divideBy = int(unparsedMonkey[3].split('by ')[1].strip(' '))
        maxValue *= divideBy
        test = parseTest(divideBy)
        indexIfTrue = int(unparsedMonkey[4].split('monkey')[1].strip(' '))
        indexIfFalse = int(unparsedMonkey[5].split('monkey')[1].strip(' '))
        res.append({
            'startingItems': startingItems,
            'operation': operation,
            'test': test,
            'indexIfTrue': indexIfTrue,
            'indexIfFalse': indexIfFalse,
            'totalInspected': 0
        })
    # YES LCM/LCD is better for maxValue, NO I don't want to fix this right now
    return res, maxValue


def parseOperation(operation):
    if operation.__contains__('*'):
        if operation.split('*')[1].__contains__('old'):
            return lambda x: int(x * x)
        else:
            return lambda x: int(x * int(operation.split('*')[1]))
    elif operation.__contains__('+'):
        if operation.split('+')[1].__contains__('old'):
            return lambda x: int(x + x)
        else:
            return lambda x: int(x + int(operation.split('+')[1]))
    else:
        raise Exception('UNABLE TO PARSE OPERATION:', operation)

def parseTest(test):
    return lambda x: x % test

def runMonkeysA(monkeys):
    for id in range(0, len(monkeys)):
        print('==============', id, '==============')
        monkey = monkeys[id]
        items = monkey.get('startingItems')
        while len(items) > 0:
            monkey['totalInspected'] += 1
            firstElemValue = items.pop(0)
            firstElemValue = monkey.get('operation')(firstElemValue)
            firstElemValue = floor(firstElemValue / 3)
            if monkey.get('test')(firstElemValue) == 0:
                monkeys[monkey.get('indexIfTrue')].get('startingItems').append(firstElemValue)
            else:
                monkeys[monkey.get('indexIfFalse')].get('startingItems').append(firstElemValue)
        for i, monkey in enumerate(monkeys):
            print(i, monkey.get('startingItems'))
    return monkeys

def runMonkeysB(monkeys, maxValue):
    for id in range(0, len(monkeys)):
        monkey = monkeys[id]
        items = monkey.get('startingItems')
        while len(items) > 0:
            monkey['totalInspected'] += 1
            firstElemValue = items.pop(0)
            firstElemValue = monkey.get('operation')(firstElemValue)
            modValue = monkey.get('test')(firstElemValue)
            if modValue == 0:
                monkeys[monkey.get('indexIfTrue')].get('startingItems').append(firstElemValue % maxValue)
            else:
                monkeys[monkey.get('indexIfFalse')].get('startingItems').append(firstElemValue % maxValue)
    return monkeys

def a(monkeys):
    for i in range(1, 21):
        monkeys = runMonkeysA(monkeys)
        print('MONKEYS AFTER ROUND', i, ':')
        for i, monkey in enumerate(monkeys):
            print(i, monkey.get('startingItems'), monkey.get('totalInspected'))
    allInspected = list(map(lambda x: x.get('totalInspected'), monkeys))
    allInspected.sort()

    print('11a: ', prod(allInspected[-2:]))


def b(monkeys, maxValue):
    for i in range(1, 10001):
        monkeys = runMonkeysB(monkeys, maxValue)
        print('MONKEYS AFTER ROUND', i, ':')
        for i, monkey in enumerate(monkeys):
            print(i, monkey.get('startingItems'), monkey.get('totalInspected'))
    allInspected = list(map(lambda x: x.get('totalInspected'), monkeys))
    allInspected.sort()

    print('11a: ', prod(allInspected[-2:]))

if __name__ == '__main__' :
    with open('./input.txt') as f:
        lines = f.read()
        unparsedMonkeys = [[y.strip(' ') for y in x.split('\n')] for x in lines.split('\n\n')]
    monkeys, maxValue = parse(unparsedMonkeys)
    # a(monkeys)
    b(monkeys, maxValue)





