import os
import re
import multiprocessing

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


points = set()
beaconsInLine = set()

info = []

for line in lines:
    text = line.strip()
    match = re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", text)
    xs = int(match.group(1))
    ys = int(match.group(2))
    xb = int(match.group(3))
    yb = int(match.group(4))
    d = manhattan(xs, ys, xb, yb)
    info.append([xs, ys, xb, yb, d])


def task(y_check):
    print(f"Testing: {y_check}")
    for block in info:
        _xs = block[0]
        _ys = block[1]
        _xb = block[2]
        _yb = block[3]
        _d = block[4]
        if _yb == y_check:
            beaconsInLine.add(_xb)
        movement = max(0, _d - abs(y_check - _ys))
        start = _xs - movement
        end = _xs + movement
        current_points = set()
        current_points.update(range(max(start, 0), min(end + 1, 4000000 + 1)))
        points.update(current_points)

    all_points = set(range(0, 4000000 + 1))
    if len(all_points) < 4000001:
        diff = all_points.difference(points)
        print(diff.pop() * 4000000 + y_check)


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        results = pool.map(task, range(0, 40 + 1))
        print("FINITO")
