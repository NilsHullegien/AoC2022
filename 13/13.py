import json
from functools import cmp_to_key


def comPairs(left, right):
    print('comPairs:', left, right)
    match left, right:
        case int(), int():
            print('ints:', left, right)
            if left > right:
                return False
            if left < right:
                return True
            if left == right:
                return None
        case list(), int():
            print('list item')
            return comPairs(left, [right])
        case int(), list():
            print('item list')
            return comPairs([left], right)
        case list(), list():
            if len(left) == 0 and len(right) == 0:
                return None
            if len(left) == 0:
                return True
            if len(right) == 0:
                return False
            compareRest = comPairs(left[0], right[0])
            if compareRest == False or compareRest == True:
                return compareRest

            return comPairs(left[1:], right[1:])
        case _:
            raise Exception('WHAT HAPPENED HERE?!', left, right)
    return False


def a(pairs):
    totalCorrect = []
    for idx, pair in enumerate(pairs):
        left = pair[0]
        right = pair[1]
        print('=======PAIR CHECKING: [', (1 + idx), ']', left, right, '=======')
        if comPairs(left, right):
            print('CORRECT PAIR: ', (1 + idx))
            totalCorrect.append(1 + idx)

    print('13a:', sum(totalCorrect))


def b(allPackets):
    allPackets.sort(key=cmp_to_key(lambda x, y: -1 if comPairs(x, y) else 1))
    print(allPackets)
    print('13b:', (allPackets.index(json.loads('[[2]]'))+1) * (allPackets.index(json.loads('[[6]]'))+1))


if __name__ == '__main__':
    with open('./input.txt') as f:
        lines = f.read()
        pairs = [[json.loads(y) for y in x.split('\n')] for x in lines.split('\n\n')]
        allPackets = [item for sublist in pairs for item in sublist]
        allPackets.append(json.loads('[[2]]'))
        allPackets.append(json.loads('[[6]]'))
        print(allPackets)
        a = []
        # a(pairs)
        b(allPackets)
