def bfs(grid):
    bfsQueue = [((0, 0), [])]
    visited = set()
    maxVal = -1
    while bfsQueue:
        currentPos, path = bfsQueue.pop(0)
        currentVal = grid[currentPos]
        if currentVal > maxVal:
            maxVal = currentVal
            # print('NEW HIGHEST VAL:', maxVal)
        visited.add(currentPos)
        if currentVal == 27:
            return path + [currentPos]

        adjacentCoords = list(
            filter(lambda z: currentVal >= grid[z] or grid[z] - currentVal == 1,
                   filter(lambda y: not visited.__contains__(y),
                          filter(lambda x: grid.__contains__(x),
                                 filter(lambda w: not path.__contains__(w), [
                                     (currentPos[0] - 1, currentPos[1]),
                                     (currentPos[0] + 1, currentPos[1]),
                                     (currentPos[0], currentPos[1] - 1),
                                     (currentPos[0], currentPos[1] + 1)
                                 ])))))
        print("CURRENT VALUE", currentVal, "CURRENTPOS", currentPos, 'ADJACENT', adjacentCoords, 'PATH:', path, 'VISITED', len(visited))

        for coord in adjacentCoords:
            bfsQueue.append((coord, path + [coord]))

    return None


if __name__ == '__main__':
    grid = {}
    with open('./example.txt') as f:
        lines = [list(line.strip('\n')) for line in f]
        for i, line in enumerate(lines):
            for j, elem in enumerate(line):
                if elem == 'S':
                    grid[(i, j)] = 1
                elif elem == 'E':
                    grid[(i, j)] = 27
                else:
                    grid[(i, j)] = ord(elem) - 96
    print(grid)
    print(len(bfs(grid)))
