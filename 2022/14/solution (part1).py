import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()


def get_coord(coordstring):
    return [int(z) for z in coordstring.split(",")]


def generate_points(a, b):
    array = []
    x1, y1 = get_coord(a)
    x2, y2 = get_coord(b)
    if x1 != x2 and y1 == y2:
        for xval in range(min(x1, x2), max(x1, x2) + 1):
            array.append(str(xval) + "," + str(y1))
    if x1 == x2 and y1 != y2:
        for yval in range(min(y1, y2), max(y1, y2) + 1):
            array.append(str(x1) + "," + str(yval))
    return array


structurePointsSet = set()

maxHeight = -100

for line in lines:
    text = line.strip()
    points = text.split(" -> ")
    firstpoint = points[0]

    for i in range(1, len(points)):
        second_point = points[i]
        x, y = get_coord(second_point)
        maxHeight = max(maxHeight, y)
        line_points = generate_points(firstpoint, second_point)
        structurePointsSet.update(line_points)
        firstpoint = second_point

print("Struttura generata")
abisso = maxHeight + 1
print(f"Abisso: {abisso}")

startingpoint = "500,0"


def compute_next_position(coord):
    _x, _y = get_coord(coord)
    new_coord = str(_x) + "," + str(_y + 1)
    if _y > abisso:
        return None

    if new_coord not in structurePointsSet:
        return new_coord

    left_down = str(_x - 1) + "," + str(_y + 1)
    if left_down not in structurePointsSet:
        return left_down

    right_down = str(_x + 1) + "," + str(_y + 1)
    if right_down not in structurePointsSet:
        return right_down

    return ""


found_roof = False
count = 0
while not found_roof:
    point = startingpoint
    while True:
        next = compute_next_position(point)
        if next == "":
            # print(f"FINE CORSA: {point}")
            structurePointsSet.add(point)
            break
        elif next is None:
            # print(f"TROVATO ABISSO: {point}")
            found_roof = True
            break
        point = next
    count += 1

print(f"Unità di sabbia: {count - 1}")
