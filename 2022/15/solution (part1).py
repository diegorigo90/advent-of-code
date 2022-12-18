import os
import re

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()

yCheck = 2000000


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


points = set()
beaconsInLine = set()

for line in lines:
    text = line.strip()
    match = re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", text)
    xs = int(match.group(1))
    ys = int(match.group(2))
    xb = int(match.group(3))
    yb = int(match.group(4))
    if yb == yCheck:
        beaconsInLine.add(xb)
    d = manhattan(xs, ys, xb, yb)
    spost = max(0, d - abs(yCheck - ys))
    start = xs - spost
    end = xs + spost
    currPoints = set()
    for x in range(start, end + 1):
        currPoints.add(x)
    points.update(currPoints)
    # print(f"Sensore: ({xs},{ys}) -> Beacon ({xb},{yb}) ----> D = {d} ---> {currPoints}")

checkPoints = len(points) - len(beaconsInLine)
print(f"POINTS: {checkPoints}")
