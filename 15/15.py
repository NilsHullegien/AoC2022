def getManhattanDistance(coordA, coordB):
    return abs(coordA[0] - coordB[0]) + abs(coordA[1] - coordB[1])



if __name__ == '__main__':
    with open('./example.txt') as f:
        rocks = set()
        unparsedCoords = [line.strip('\n').strip('Sensor at x=').split(': closest beacon is at x=') for line in f]
        lines = []
        for coords in unparsedCoords:
            print(coords)
            sensorCoords = list(map(lambda x: int(x), coords[0].split(', y=')))
            beaconCoords = list(map(lambda x: int(x), coords[1].split(', y=')))
            print(sensorCoords, beaconCoords)
            lines.append((sensorCoords, beaconCoords))
        print(lines)


        # gridDimensions = [minX, maxX, minY, maxY]
        # for row:
        #     for each coordinate, is it within the MANHATTAN distance of any scanner (count NOT)
