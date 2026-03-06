from collections import deque

graph = {
    "S": [("B1", 2), ("C", 4), ("B2", 4)],
    "B1": [("G", 5), ("C", 5)],
    "B2": [("C", 1)],
    "E": [("B2", 4)],
    "C": [("G", 3), ("F", 3)],
    "F": [("B2", 1)],
    "G": [("C", 2)]
}

# Heuristic function 
def h(n):
    return 0   # reduces A* to Dijkstra


def bfs(start, goal):

    visited = []
    queue = deque([[start]])
    expanded = 0

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node not in visited:

            visited.append(node)
            expanded += 1

            if node == goal:
                return path, expanded

            for neighbor, weight in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None, expanded


def dfs(start, goal):

    visited = []
    stack = [[start]]
    expanded = 0

    while stack:

        path = stack.pop()
        node = path[-1]

        if node not in visited:

            visited.append(node)
            expanded += 1

            if node == goal:
                return path, expanded

            for neighbor, weight in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    
    return None, expanded



def astar(start, goal):

    openSet = [start]
    cameFrom = {}

    gScore = {node: float("inf") for node in graph}
    gScore[start] = 0

    fScore = {node: float("inf") for node in graph}
    fScore[start] = h(start)

    expanded = 0

    while openSet:

        current = min(openSet, key=lambda node: fScore[node])
        expanded += 1

        if current == goal:

            path = [current]

            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)

            path.reverse()
            return path, expanded, gScore[goal]

        openSet.remove(current)

        for neighbor, weight in graph[current]:

            tentative = gScore[current] + weight

            if tentative < gScore[neighbor]:

                cameFrom[neighbor] = current
                gScore[neighbor] = tentative
                fScore[neighbor] = gScore[neighbor] + h(neighbor)

                if neighbor not in openSet:
                    openSet.append(neighbor)
    
    return None, expanded, float('inf')


start = "S"
goal = "G"

print("BFS:")
path, expanded = bfs(start, goal)
print("Path:", path)
print("Expanded Nodes:", expanded)

print("\nDFS:")
path, expanded = dfs(start, goal)
print("Path:", path)
print("Expanded Nodes:", expanded)

print("\nA*:")
path, expanded, cost = astar(start, goal)
print("Path:", path)
print("Expanded Nodes:", expanded)
print("Total Cost:", cost)