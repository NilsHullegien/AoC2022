with open('./input.txt') as f:
    lines = [line.strip('\n') for line in f]


def checkVisibleTreesRow(grid, i, row):
    highestTree = -1
    for j, tree in enumerate(row):
        if grid[(i, j)] == 0 and tree > highestTree:
            grid[(i, j)] = 1
        if tree > highestTree:
            highestTree = tree


def checkReverseVisibleTreesRow(grid, i, row):
    highestTree = -1
    row.reverse()
    for j, tree in enumerate(row):
        if grid[(i, len(row) - j - 1)] == 0 and tree > highestTree:
            grid[(i, len(row) - j - 1)] = 1
        if tree > highestTree:
            highestTree = tree



def checkVisibleTreesColumn(grid, i, column):
    highestTree = -1
    for j, tree in enumerate(column):
        if grid[(j, i)] == 0 and tree > highestTree:
            grid[(j, i)] = 1
        if tree > highestTree:
            highestTree = tree


def checkReverseVisibleTreesColumn(grid, i, column):
    highestTree = -1
    column.reverse()
    for j, tree in enumerate(column):
        if grid[(len(column) - j - 1, i)] == 0 and tree > highestTree:
            grid[(len(column) - j - 1, i)] = 1
        if tree > highestTree:
            highestTree = tree


grid = {}
for i, line in enumerate(lines):
    row = map(int, [*line])
    for j, tree in enumerate(row):
        grid[(i, j)] = 0

for i, line in enumerate(lines):
    row = list(map(int, [*line]))
    checkVisibleTreesRow(grid, i, row)
    checkReverseVisibleTreesRow(grid, i, row)

columns = [[row[i] for row in lines] for i in range(len(lines[0]))]
for i, line in enumerate(columns):
    column = list(map(int, [*line]))
    checkVisibleTreesColumn(grid, i, column)
    checkReverseVisibleTreesColumn(grid, i, column)

print(grid)
print("8a (should be 1733):", len(list(filter(lambda x: x == 1, grid.values()))))
