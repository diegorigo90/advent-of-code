import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()


def get_point(_text):
    return [int(v) for v in _text.split(",")]


points = []

for line in lines:
    text = line.strip()
    points.append(text)


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


def get_nearest_points(_pt):
    [_x, _y, _z] = get_point(_pt)
    _points = []
    if min_x-1 <= _x+1 <= max_x+1:
        _points.append(tostring(_x+1, _y, _z))
    if min_x-1 <= _x-1 <= max_x+1:
        _points.append(tostring(_x-1, _y, _z))
    if min_y-1 <= _y+1 <= max_y+1:
        _points.append(tostring(_x, _y+1, _z))
    if min_y-1 <= _y-1 <= max_y+1:
        _points.append(tostring(_x, _y-1, _z))
    if min_z-1 <= _z+1 <= max_z+1:
        _points.append(tostring(_x, _y, _z+1))
    if min_z-1 <= _z-1 <= max_z+1:
        _points.append(tostring(_x, _y, _z-1))
    return _points


visited = set()
to_visit = set()
to_visit.add(tostring(min_x, min_y, min_z))
surface = set()
touched_surfaces = 0
while True:
    next_visit = set()
    for pt in to_visit:
        print(f"{len(to_visit)} da visitare, {len(visited)} visitati, {len(surface)} superficiali")

        near_points = get_nearest_points(pt)
        touch_surface = False
        for pt1 in near_points:
            if pt1 not in visited:
                if pt1 in points:
                    touch_surface = True
                    touched_surfaces += 1
                else:
                    next_visit.add(pt1)
        if touch_surface:
            surface.add(pt)
        visited.add(pt)
    to_visit = next_visit
    if len(to_visit) == 0:
        break

print(touched_surfaces)
