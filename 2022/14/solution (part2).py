import os
import time

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\input.txt',"r")
lines = f.readlines()


def coords(coordstring):
    return [int(z) for z in coordstring.split(",")]

def generatepoints(a,b):
    array = []
    x1,y1 = coords(a)
    x2,y2 = coords(b)
    if (x1 != x2 and y1 == y2):
        for xval in range(min(x1,x2),max(x1,x2)+1):
            array.append(str(xval) + "," + str(y1))
    if (x1 == x2 and y1 != y2):
        for yval in range(min(y1,y2),max(y1,y2)+1):
            array.append(str(x1) + "," + str(yval))
    return array


structurePointsSet = set()

maxHeight = -100

for line in lines:
    text = line.strip()
    points = text.split(" -> ")
    firstpoint = points[0]
    
    for i in range(1,len(points)):
        secondpoint = points[i]
        x,y = coords(secondpoint)
        maxHeight = max(maxHeight,y)
        linepoints = generatepoints(firstpoint, secondpoint)
        structurePointsSet.update(linepoints)
        firstpoint = secondpoint

print("Struttura generata")
fondo = maxHeight + 2
print(f"Fondo: {fondo}")

startingpoint = "500,0"

def computenextposition(coord):
    x,y = coords(coord)
    newCoord = str(x) + "," + str(y+1)
    
    if y > fondo:
        return "ALERT"

    if y == (fondo - 1):
        return ""
    
    if not newCoord in structurePointsSet:
        return newCoord
    
    leftDown = str(x-1) + "," + str(y+1)
    if not leftDown in structurePointsSet:
        return leftDown
    
    rightDown = str(x+1) + "," + str(y+1)
    if not rightDown in structurePointsSet:
        return rightDown

    return ""

fermaTutto = False
count = 0
while not fermaTutto:
    point = startingpoint
    while True:
        next = computenextposition(point)
        if next == "":
            structurePointsSet.add(point)
            if point == startingpoint:
                fermaTutto = True
            break
        point = next
    count += 1
    if len(structurePointsSet) % 100 == 0:
        print(f"Elementi totali: {len(structurePointsSet)}")

print(f"Unità di sabbia totali: {count}")

