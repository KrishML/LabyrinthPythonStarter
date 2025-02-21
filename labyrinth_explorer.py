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
    # Constants for readability
    INFINITY = float('inf')
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Allowed movement directions
    costs = {'.': 1, 'S': 1, 'E': 1, '*': 0, 'M': 5, '#': 10000000}

    def get_position(graph, target):
        """Find the position of a target element ('S', 'E') in the graph."""
        coords = np.where(graph == target)
        return tuple(zip(*coords))[0]  # Convert coordinates to a tuple

    # Convert the labyrinth into a numpy array
    graph = np.array(labyrinth)
    labyrinth_shape = graph.shape
    rows, cols = labyrinth_shape

    # Get the start and end positions
    start_position = get_position(graph, 'S')
    end_position = get_position(graph, 'E')
    print(start_position, end_position)  # Debugging print

    # Priority queue for Dijkstra's algorithm
    pq = [(0, start_position)]
    distances = {start_position: 0}  # Track shortest distances
    visited = set()  # Set to track visited nodes
    previous_nodes = {}

    # Dijkstra's algorithm main loop
    while pq:
        print('Current priority queue:', pq)  # Debugging print
        current_cost, (x, y) = heapq.heappop(pq)

        if (x, y) == end_position:  # Stop when reaching the goal
            break

        visited.add((x, y))  # Mark the current node as visited
        for dx, dy in movements:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:  # Check bounds
                new_cost = current_cost + costs.get(graph[nx, ny], INFINITY)
                if new_cost < distances.get((nx, ny), INFINITY):  # Check for a better path
                    distances[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))
                    previous_nodes[(nx, ny)] = (x, y)

    # Backtrack from the end to find the path
    path = []
    current = end_position
    while current in previous_nodes:
        path.append(current)
        current = previous_nodes[current]
    path.append(start_position)
    path.reverse()

    return path

def print_path(labyrinth, path):
    path_set = set(path)
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if (i, j) in path_set:
                print('>', end=' ')
            else:
                print(labyrinth[i][j], end=' ')
        print()
labyrinth = load_labyrinth("labyrinth_9x9.txt")
print("Labyrinth loaded:")
printlab(labyrinth)
# labyrinth=convertlab(labyrinth)
# printlab(labyrinth)
path=dijkstra(labyrinth)
print(path)
print("Labyrinth with path:")
print_path(labyrinth, path)