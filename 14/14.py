def getStones(first, second):
    if first[0] == second[0]:
        a = int(first[1])
        b = int(second[1])
        min = a
        max = b
        if (min > b):
            min = b
            max = a
        yCoordList = set((int(first[0]), y) for y in range(min, max+1))
        return yCoordList
    a = int(first[0])
    b = int(second[0])
    min = a
    max = b
    if (min > b):
        min = b
        max = a
    xCoordList = set((x, int(first[1])) for x in range(min, max + 1))
    return xCoordList

def pourSand(rocks, abyssLevel):
    obstacles = rocks
    totalSand = 0
    print(abyssLevel)
    currentPos = (500, 0)
    abyssReached = False
    while not abyssReached:
        stopped = False
        while not stopped:
            if currentPos[1] == abyssLevel:
                abyssReached = True
                break
            hypotheticalPos = (currentPos[0], currentPos[1] + 1)
            if not obstacles.__contains__(hypotheticalPos):
                currentPos = hypotheticalPos
                continue
            hypotheticalPos = (currentPos[0] - 1, currentPos[1] + 1)
            if not obstacles.__contains__(hypotheticalPos):
                currentPos = hypotheticalPos
                continue
            hypotheticalPos = (currentPos[0] + 1, currentPos[1] + 1)
            if not obstacles.__contains__(hypotheticalPos):
                currentPos = hypotheticalPos
                continue
            stopped = True
        if not abyssReached:
            print('SAND PLACED AT', currentPos)
            totalSand += 1
            obstacles.add(currentPos)
            currentPos = (500, 0)
    print('14a:', totalSand)




if __name__ == '__main__':
    with open('./input.txt') as f:
        rocks = set()
        lines = [line.strip('\n') for line in f]
        coords = [x.split(' -> ') for x in lines]
        for coord in coords:
            for i in range(len(coord) - 1):
                pair = coord[i:i+2]
                rocks.update(getStones(pair[0].split(','), pair[1].split(',')))
        abyssLevel = max(rocks, key=lambda x: x[1])[1]
        pourSand(rocks, abyssLevel)
