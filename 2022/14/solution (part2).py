import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()


def get_coordinates(coordstring):
    return [int(z) for z in coordstring.split(",")]


def generate_points(a, b):
    array = []
    x1, y1 = get_coordinates(a)
    x2, y2 = get_coordinates(b)
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
    first_point = points[0]

    for i in range(1, len(points)):
        second_point = points[i]
        x, y = get_coordinates(second_point)
        maxHeight = max(maxHeight, y)
        line_points = generate_points(first_point, second_point)
        structurePointsSet.update(line_points)
        first_point = second_point

print("Struttura generata")
roof = maxHeight + 2
print(f"Fondo: {roof}")

starting_point = "500,0"


def compute_next_position(coord):
    _x, _y = get_coordinates(coord)
    new_coordinates = str(_x) + "," + str(_y + 1)

    if _y > roof:
        return "ALERT"

    if _y == (roof - 1):
        return ""

    if new_coordinates not in structurePointsSet:
        return new_coordinates

    left_down = str(_x - 1) + "," + str(_y + 1)
    if left_down not in structurePointsSet:
        return left_down

    right_down = str(_x + 1) + "," + str(_y + 1)
    if right_down not in structurePointsSet:
        return right_down

    return ""


stop = False
count = 0
while not stop:
    point = starting_point
    while True:
        next_position = compute_next_position(point)
        if next_position == "":
            structurePointsSet.add(point)
            if point == starting_point:
                stop = True
            break
        point = next_position
    count += 1
    if len(structurePointsSet) % 100 == 0:
        print(f"Elementi totali: {len(structurePointsSet)}")

print(f"Unità di sabbia totali: {count}")
