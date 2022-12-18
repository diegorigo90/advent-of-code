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


max_x = -1000
max_y = -1000
max_z = -1000
min_x = 1000
min_y = 1000
min_z = 1000
for point in points:
    [x, y, z] = get_point(point)
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    max_z = max(z, max_z)

    min_x = min(x, min_x)
    min_y = min(y, min_y)
    min_z = min(z, min_z)

print(f"{min_x}/{max_x} - {min_y}/{max_y} - {min_z}/{max_z}")
points_coord = [get_point(p) for p in points]
surface = 0
