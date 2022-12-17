import os
import re
import multiprocessing

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\input.txt',"r")
lines = f.readlines()


def manhattan(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

points = set()
beaconsInLine = set()

info = []

for line in lines:
    text = line.strip()
    match = re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)",text)
    xs = int(match.group(1))
    ys = int(match.group(2))
    xb = int(match.group(3))
    yb = int(match.group(4))
    d = manhattan(xs,ys,xb,yb)
    info.append([xs,ys,xb,yb,d])


def task(yCheck):
    print(f"Testing: {yCheck}")
    for block in info:
        xs = block[0]
        ys = block[1]
        xb = block[2]
        yb = block[3]
        d = block[4]
        if yb == yCheck:
            beaconsInLine.add(xb)
        spost = max(0, d - abs(yCheck -ys))
        start = xs - spost
        end = xs + spost
        currPoints = set()
        currPoints.update(range(max(start, 0), min(end + 1,4000000 + 1)))
        points.update(currPoints)

    allPoints = set(range(0,4000000 +1))
    size = len(allPoints)
    # print(size)
    if len(allPoints) < 4000001:
        diff = allPoints.difference(points)
        print(diff.pop() * 4000000 + yCheck)

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        results = pool.map(task, range(0,40 +1))
        print("FINITO")