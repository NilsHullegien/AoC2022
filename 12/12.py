import networkx as nx
from networkx import NetworkXNoPath

grid = {}
graph = nx.DiGraph()
start = None
starts = []
end = None
with open('./input.txt') as f:
    lines = [list(line.strip('\n')) for line in f]

    for i, line in enumerate(lines):
        for j, elem in enumerate(line):
            graph.add_node((i, j))
            if elem == 'a':
                starts.append((i, j))
            if elem == 'S':
                start = (i, j)
                starts.append((i, j))
                grid[(i, j)] = 1
            elif elem == 'E':
                end = (i, j)
                grid[(i, j)] = 26
            else:
                grid[(i, j)] = ord(elem) - 96
    for coord in grid:
        currentVal = grid[coord]
        adjacentCoords = list(
            filter(lambda z: currentVal >= grid[z] or grid[z] - currentVal == 1,
                   filter(lambda x: grid.__contains__(x), [
                              (coord[0] - 1, coord[1]),
                              (coord[0] + 1, coord[1]),
                              (coord[0], coord[1] - 1),
                              (coord[0], coord[1] + 1)
                          ])))
        for adjacentCoord in adjacentCoords:
            graph.add_edge(coord, adjacentCoord)
    print('12a:', nx.dijkstra_path_length(graph, start, end))
    minDist = 90000000
    for x in starts:
        try:
            minDist = min(minDist, nx.dijkstra_path_length(graph, x, end))
        except NetworkXNoPath:
            continue


    print('12b:', minDist)


