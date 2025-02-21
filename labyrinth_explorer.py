import sys
import numpy as np
import heapq

def load_labyrinth(filename):
    
    with open(filename, "r") as f:
        lines = f.readlines()

    labyrinth = [list(line.strip()) for line in lines]
    return labyrinth


def printlab(labyrinth):
    for i in range(len(labyrinth)):
        print(labyrinth[i])


def dijkstra(labyrinth):
    graph = np.array(labyrinth)
    l,w = graph.shape
    # swh = np.where(graph == 'S')
    # start = coords = list(zip(*swh))
    # ewh = np.where(graph == 'E')
    # end = coords = list(zip(*ewh))
    # Convert coordinates to tuples instead of lists
    swh = np.where(graph == 'S')
    # print(swh)
    start = tuple(zip(*swh))[0]
    print(start)
    ewh = np.where(graph == 'E')
    end = tuple(zip(*ewh))[0]
    print(end)


    #we keep the cost and the position in the heap

    pq = [(0, start)]
    # print(type(pq))  
    distances = {start: 0}
    previous_nodes = {}
    visited = set()

    # movements
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    costs = {
        '.': 1,   
        'S': 1,   
        'E': 1,   
        '*': 0,   
        'M': 5,   
        '#': 10000000
    }

    while pq:
        print('the current priority queue is:', pq)
        current_cost, (x, y) = heapq.heappop(pq)

        if (x, y) == end:
            break  # break at goal

        visited.add((x, y)) # add the current node to the set of visited as it is already examined

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < w:
                new_cost = current_cost + costs.get(graph[nx, ny], float('inf'))
                if new_cost < distances.get((nx, ny), float('inf')):
                    distances[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))
                    previous_nodes[(nx, ny)] = (x, y)


    path = []
    current = end
    while current in previous_nodes:
        path.append(current)
        current = previous_nodes[current]
    path.append(start)
    path.reverse()
    return path

def print_path(labyrinth, path):
    path_set = set(path)
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if (i, j) in path_set:
                print('P', end=' ')
            else:
                print(labyrinth[i][j], end=' ')
        print()
labyrinth = load_labyrinth("labyrinth_5x5.txt")
print("Labyrinth loaded:")
printlab(labyrinth)
# labyrinth=convertlab(labyrinth)
# printlab(labyrinth)
path=dijkstra(labyrinth)
print(path)
print("Labyrinth with path:")
print_path(labyrinth, path)