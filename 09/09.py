with open('./input.txt') as f:
    input = [line.strip('\n') for line in f]
    lines = [x.split() for x in input]


def moveHead(direction, head):
    newPosHead = head
    match direction:
        case 'U':
            newPosHead = (head[0], head[1] + 1)
        case 'D':
            newPosHead = (head[0], head[1] - 1)
        case 'L':
            newPosHead = (head[0] - 1, head[1])
        case 'R':
            newPosHead = (head[0] + 1, head[1])
    return newPosHead


def moveTail(newPosHead, tail):
    # print('MOVE TAIL', newPosHead, tail)
    distX = abs(tail[0] - newPosHead[0])
    distY = abs(tail[1] - newPosHead[1])

    if distX > 1 or distY > 1:
        # print('match', (newPosHead[0] - tail[0], newPosHead[1] - tail[1]))
        match (newPosHead[0] - tail[0], newPosHead[1] - tail[1]):
            case (1, 2) | (2, 1) | (2, 2):
                return tail[0] + 1, tail[1] + 1
            case (-1, 2) | (-2, 1)| (-2, 2):
                return tail[0] - 1, tail[1] + 1
            case (1, -2) | (2, -1) | (2, -2):
                return tail[0] + 1, tail[1] - 1
            case (-1, -2) | (-2, -1) | (-2, -2):
                return tail[0] - 1, tail[1] - 1
            case (0, 2):
                return tail[0], tail[1] + 1
            case (0, -2):
                return tail[0], tail[1] - 1
            case (2, 0):
                return tail[0] + 1, tail[1]
            case (-2, 0):
                return tail[0] - 1, tail[1]
            case _:
                print('something went wrong!')
                print((newPosHead[0] - tail[0], newPosHead[1] - tail[1]))
    else:
        return tail

#
# def a(posHead, posTail):
#     uniqueCoords = set()
#     for line in lines:
#         direction = line[0]
#         for _ in range(0, int(line[1])):
#             posHead = moveHead(direction, posHead)
#             posTail = moveTail(posHead, posTail)
#             print(posHead, posTail)
#             uniqueCoords.add(posTail)
#     print('9a:', len(uniqueCoords))


def b():
    uniqueCoords = set()
    rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

    for line in lines:
        direction = line[0]
        print(line)
        for _ in range(0, int(line[1])):
            posHead = moveHead(direction, rope[0])
            rope[0] = posHead
            for i in range(1, 10):
                new = moveTail(rope[i - 1], rope[i])
                if rope[i] == new:
                    break
                rope[i] = new
                print(i, rope)
            uniqueCoords.add(rope[9])
            print(rope)
            print('===================')
        print(rope)

    print('9b: ', len(uniqueCoords))


if __name__ == '__main__':
    # posHead = (0, 0)
    # posTail = (0, 0)
    # a((0, 0), (0, 0))
    b()
