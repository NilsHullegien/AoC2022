with open('08/example.txt') as f:
    lines = [line.strip('\n') for line in f];

def checkVisibleTreesRow(grid, i, row):
    highestTree = -1;
    for j, tree in enumerate(row):
        if grid[(i, j)] == 1:
            break;
        if tree > highestTree:
            grid[(i, j)] = 1;
            highestTree = tree;
        else:
            grid[(i, j)] = 0;

def checkReverseRowVisibleTreesRow(grid, i, row):
    highestTree = -1;
    row.reverse();
    for j, tree in enumerate(row):
        if grid[(i, len(row) - j - 1)] == 1:
            break;
        if tree > highestTree:
            grid[(i, len(row) - j - 1)] = 1;
            highestTree = tree;
        else:
            grid[(i, len(row) - j - 1)] = 0;
            
def checkVisibleTreesColumn(grid, i, column):
    highestTree = -1;
    for j, tree in enumerate(column):
        if grid[(j, i)] == 1:
            break;
        if tree > highestTree:
            grid[(j, i)] = 1;
            highestTree = tree;
        else:
            grid[(j, i)] = 0;

def checkReverseRowVisibleTreesColumn(grid, i, column):
    highestTree = -1;
    column.reverse();
    for j, tree in enumerate(column):
        if grid[(len(column) - j - 1, i)] == 1:
            break;
        if tree > highestTree:
            grid[(len(column) - j - 1, i)] = 1;
            highestTree = tree;
        else:
            grid[(len(column) - j - 1, i)] = 0;

grid = {}
for i, line in enumerate(lines):
    row = map(int, [*line])
    for j, tree in enumerate(row):
        grid[(i,j)] = None;

for i, line in enumerate(lines):
    row = list(map(int, [*line]));
    checkVisibleTreesRow(grid, i, row);
    checkReverseRowVisibleTreesRow(grid, i, row);

columns = [[row[i] for row in lines] for i in range(len(lines[0]))]
for i, line in enumerate(columns):
    column = list(map(int, [*line]));
    checkVisibleTreesColumn(grid, i, column);
    checkReverseRowVisibleTreesColumn(grid, i, column);

print(grid);
print("8a:", len(list(filter(lambda x : x == 1, grid.values()))));


