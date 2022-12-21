import json


def comPairs(leftHead, leftTail, rightHead, rightTail):
    print(leftHead, leftTail, rightHead, rightTail)
    match leftHead, rightHead:
        case None, None:
            return True
        case None, _:
            return True
        case _, None:
            return False
        case int(), int():
            print('ints:', leftHead, leftTail, rightHead, rightTail)
            if leftHead > rightHead:
                return False
            if leftHead < rightHead:
                return True
            if leftTail == rightTail:
                return True
            if len(leftTail) == 0:
                return False
            if len(rightTail) == 0:
                return True
            return comPairs(leftTail[0], leftTail[1:], rightTail[0], rightTail[1:])
        case list(), int():
            print('list item')
            return comPairs(leftHead, leftTail, [rightHead], rightTail)
        case int(), list():
            print('item list')
            return comPairs([leftHead], leftTail, rightHead, rightTail)
        case list(), list():
            if comPairs(leftHead[0], leftHead[1:], rightHead[0], rightHead[1:]):
                if leftTail == rightTail:
                    return True
                if len(leftTail) == 0:
                    return False
                if len(rightTail) == 0:
                    return True
                return comPairs(leftTail[0], leftTail[1:], rightTail[0], rightTail[1:])
            return False
        case _:
            raise Exception('WHAT HAPPENED HERE?!', leftHead, leftTail, rightHead, rightTail)
    return False


if __name__ == '__main__':
    with open('./example.txt') as f:
        lines = f.read()
        pairs = [[json.loads(y) for y in x.split('\n')] for x in lines.split('\n\n')]
        print(pairs)

        totalCorrect = 0
        for idx, pair in enumerate(pairs):
            left = pair[0]
            right = pair[1]
            print('PAIR CHECKING:', left, right)
            if comPairs(left[0], left[1:], right[0], right[1:]):
                print('CORRECT PAIR: ', (1 + idx))
                totalCorrect += (1 + idx)

        print(totalCorrect)
