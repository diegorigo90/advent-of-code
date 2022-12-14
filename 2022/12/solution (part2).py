import os
import numpy as np
import time

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\input.txt',"r")

def nearChars(destChar, currChar):
    
    if destChar == "S":
        destChar = "a"
    if destChar == "E":
        destChar = "z"

    if currChar == "S":
        currChar = "a"
    if currChar == "E":
        currChar = "z"
    return abs(ord(str(destChar)) <= (ord(str(currChar))) + 1)

def getIndexCode(idx1,idx2):
    return str(idx1) + "/" + str(idx2)

M = []

for line in f.readlines():
    text = line.strip()
    M.append([*text])

arr=np.array(M)
start = np.where(arr == "S")
end = np.where(arr == "E")
n, m = arr.shape
i = start[0][0]
j = start[1][0]
iEnd = end[0][0]
jEnd = end[1][0]

endIdx = getIndexCode(iEnd,jEnd)
startIdx = getIndexCode(i,j)
startingPoints = [startIdx]
startEl = arr[i,j]
nodes = [(i,j)]

graph = {}

for idx in range(0,arr.size):
    j = (idx % m + 1) - 1
    i = (idx // m + 1) - 1
    el = arr[i,j]
    # print(f"{idx} -> {i}/{j}")
    iBefore = max(0,min(i-1,n-1))
    iAfter = max(0,min(i+1,n-1))
    jBefore = max(0,min(j-1,m-1))
    jAfter = max(0,min(j+1,m-1))
    elTop = None
    elBottom = None
    elLeft = None
    elRight = None
    if (iBefore < i):
        elTop = arr[iBefore, j]
    if (iAfter > i):
        elBottom = arr[iAfter, j]
    if (jBefore < j):
        elLeft = arr[i, jBefore]
    if (jAfter > j):
        elRight = arr[i, jAfter]
    # PRINT NEIGHBORS
    # print(f"[ ] [{elTop}] [ ]")
    # print(f"[{elLeft}] [{el}] [{elRight}]")
    # print(f"[ ] [{elBottom}] [ ]")

    possibles = []
    if elTop is not None and nearChars(elTop,el):
        possibles.append(getIndexCode(iBefore,j))
    if elBottom is not None and nearChars(elBottom,el):
        possibles.append(getIndexCode(iAfter,j))
    if elLeft is not None and nearChars(elLeft,el):
        possibles.append(getIndexCode(i,jBefore))
    if elRight is not None and nearChars(elRight,el):
        possibles.append(getIndexCode(i,jAfter))
    # print(f"{i}/{j} -> {possibles}")
    graph[getIndexCode(i,j)] = possibles
    if el == "a":
        startingPoints.append(getIndexCode(i,j))


visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, neighboursMap, node): #function for BFS
    visited = [node]
    queue = [node]

    count = 0
    while queue:          
        nextQueue = []
        count += 1
        # print(f"Giro {count}")
        for elem in queue:
            # print(f"ELEMENT: {elem} -> {neighboursMap[elem]}")
            for neighbour in neighboursMap[elem]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    nextQueue.append(neighbour)
                    # print(f"NEIGHBOR: {neighbour} ({endIdx})")
                    if neighbour == endIdx:
                        print("ARRIVATO")
                        print(f"Totale passaggi: {count}")
                        return count
        queue = nextQueue
    

# Driver Code
print("Following is the Breadth-First Search")
minimum = 10000000000

for point in startingPoints:
    count = bfs(visited, graph, point)    # function calling
    
    if count is not None:
        minimum = min(minimum,count)
print(minimum)