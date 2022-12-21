import os
import re
import multiprocessing

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\input.txt', "r")
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

CONST = 4000000


def task(yCheck):
    if yCheck > 0 and yCheck % 80000 == 0:
        print(f"Testing: {yCheck}")

    li = []
    for block in info:
        xs = block[0]
        ys = block[1]
        d = block[4]
        dist = abs(yCheck - ys)
        if dist <= d:
            spost = d - dist
            start = xs - spost
            end = xs + spost
            li.append({
                "val": start,
                "type": "S"
            })
            li.append({
                "val": end,
                "type": "E"
            })

    li.sort(key=lambda x: x.get('val'))
    if li[0]['val'] > 0:
        print(f"PRIMO ITEM POSITIVO -> {yCheck}")
    if li[len(li) - 1]['val'] < CONST:
        print(f"ULTIMO ITEM MINORE DI {CONST} -> {yCheck}")
    stack = 0
    firstitem = True
    lastItem = -100
    stacklist = []
    for obj in li:
        if not firstitem and stack == 0:
            if abs(obj['val'] - lastItem) > 1:
                x = obj['val']
                tuningfreq = (x - 1) * 4000000 + yCheck
                print(f"TROVATO ({x},{yCheck}): {tuningfreq}")
        if obj['type'] == "S":
            stack += 1
            stacklist.append(stack)
        elif stack < 0:
            print("WARNING: stack negativo")
        else:
            stack -= 1
            lastItem = obj['val']
        firstitem = False


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        results = pool.map(task, range(0, CONST + 1))
        print("FINITO")

# for i in range(0,100000):
#     task(i)
