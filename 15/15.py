class Sensor:
    def __init__(self, sensorCoords, manDist):
        self.sensorCoords = sensorCoords
        self.manDist = manDist

    def display(self):
        print('=================')
        print('coords', self.sensorCoords)
        print('manDist', self.manDist)
        print('=================')

def getManhattanDistance(coordA, coordB):
    return abs(coordA[0] - coordB[0]) + abs(coordA[1] - coordB[1])

def findPosWithoutBeacon(rowId, sensorList, rangeCoords):
    totalWithoutBeacon = 0
    for i in range(rangeCoords[0], rangeCoords[1] + 1):
        inRange = False
        for sensor in sensorList:
            if inRange:
                break
            inRange = (getManhattanDistance((i, rowId), sensor.sensorCoords) <= sensor.manDist)
        if inRange:
            print(i)
            totalWithoutBeacon += 1
    return totalWithoutBeacon


if __name__ == '__main__':
    with open('./input.txt') as f:
        # rowToCheck = 10
        rowToCheck = 2000000
        unparsedCoords = [line.strip('\n').strip('Sensor at x=').split(': closest beacon is at x=') for line in f]
        sensorList = []
        beaconsInCheckedRow = set()
        maxX = -9999999999999999999999
        minX = 99999999999999999999999
        for coords in unparsedCoords:
            sensorCoord = list(map(lambda x: int(x), coords[0].split(', y=')))
            beaconCoord = list(map(lambda x: int(x), coords[1].split(', y=')))
            if beaconCoord[1] == rowToCheck:
                print(beaconCoord)
                beaconsInCheckedRow.add(beaconCoord[0])
            sensorList.append(Sensor(sensorCoord, getManhattanDistance(sensorCoord, beaconCoord)))
            posX = beaconCoord[0]
            if posX < minX:
                minX = posX
            elif posX > maxX:
                maxX = posX

        # for sensor in sensorList:
        #     sensor.display()
        print((minX, maxX))
        print('Test 15a:', (findPosWithoutBeacon(rowToCheck, sensorList, (minX, maxX)) - len(beaconsInCheckedRow)))



        # gridDimensions = [minX, maxX, minY, maxY]
        # for row:
        #     for each coordinate, is it within the MANHATTAN distance of any scanner (count NOT)
