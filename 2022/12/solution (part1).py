import os

import numpy as np

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")


def near_chars(dest_char, curr_char):
    if dest_char == "S":
        dest_char = "a"
    if dest_char == "E":
        dest_char = "z"

    if curr_char == "S":
        curr_char = "a"
    if curr_char == "E":
        curr_char = "z"
    return abs(ord(str(dest_char)) <= (ord(str(curr_char))) + 1)


def get_index_code(idx1, idx2):
    return str(idx1) + "/" + str(idx2)


M = []

for line in f.readlines():
    text = line.strip()
    M.append([*text])

arr = np.array(M)
start = np.where(arr == "S")
end = np.where(arr == "E")
n, m = arr.shape
i = start[0][0]
j = start[1][0]
iEnd = end[0][0]
jEnd = end[1][0]

endIdx = get_index_code(iEnd, jEnd)
startIdx = get_index_code(i, j)
startEl = arr[i, j]
nodes = [(i, j)]

graph = {}

for idx in range(0, arr.size):
    j = (idx % m + 1) - 1
    i = (idx // m + 1) - 1
    el = arr[i, j]
    # print(f"{idx} -> {i}/{j}")
    iBefore = max(0, min(i - 1, n - 1))
    iAfter = max(0, min(i + 1, n - 1))
    jBefore = max(0, min(j - 1, m - 1))
    jAfter = max(0, min(j + 1, m - 1))
    elTop = None
    elBottom = None
    elLeft = None
    elRight = None
    if iBefore < i:
        elTop = arr[iBefore, j]
    if iAfter > i:
        elBottom = arr[iAfter, j]
    if jBefore < j:
        elLeft = arr[i, jBefore]
    if jAfter > j:
        elRight = arr[i, jAfter]

    possibles = []
    if elTop is not None and near_chars(elTop, el):
        possibles.append(get_index_code(iBefore, j))
    if elBottom is not None and near_chars(elBottom, el):
        possibles.append(get_index_code(iAfter, j))
    if elLeft is not None and near_chars(elLeft, el):
        possibles.append(get_index_code(i, jBefore))
    if elRight is not None and near_chars(elRight, el):
        possibles.append(get_index_code(i, jAfter))
    # print(f"{i}/{j} -> {possibles}")
    graph[get_index_code(i, j)] = possibles

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(_visited, _neighbours_map, node):  # function for BFS
    _visited = [node]
    _queue = [node]

    count = 0
    while _queue:
        _next_queue = []
        count += 1
        # print(f"Giro {count}")
        for elem in _queue:
            # print(f"ELEMENT: {elem} -> {neighboursMap[elem]}")
            for neighbour in _neighbours_map[elem]:
                if neighbour not in _visited:
                    _visited.append(neighbour)
                    _next_queue.append(neighbour)
                    # print(f"NEIGHBOR: {neighbour} ({endIdx})")
                    if neighbour == endIdx:
                        print("ARRIVATO")
                        print(f"Totale passaggi: {count}")
        _queue = _next_queue


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, startIdx)  # function calling
