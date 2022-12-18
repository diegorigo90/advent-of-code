import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()


def get_point(_text):
    return [int(v) for v in _text.split(",")]


points = {}

for line in lines:
    text = line.strip()
    points[text] = "OK"


def tostring(_x, _y, _z):
    return str(_x) + "," + str(_y) + "," + str(_z)


def count_nears(_point, _points):
    [x, y, z] = get_point(_point)
    count = 0

    points_to_check = [
        tostring(x, y, z + 1),
        tostring(x, y, z - 1),
        tostring(x + 1, y, z),
        tostring(x - 1, y, z),
        tostring(x, y - 1, z),
        tostring(x, y + 1, z)]
    for checkpoint in points_to_check:
        if points.get(checkpoint) is not None:
            count += 1
    return count

surface = 0

for point in points:
    surface += (6 - count_nears(point, points))

print(surface)
