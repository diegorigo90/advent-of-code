import os
import re

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\\input.txt', 'r')
Lines = file1.readlines()

topInfo = True
config = []
N = 9
for j in range(1, N+1):
    config.append([])

for line in Lines:
    if " 1 " in line:
        topInfo = False

    if topInfo:
        for i in range(0, N):
            el = line[1+4*i]
            if el.strip() != "":
                config[i].insert(0, el)
                print(f"{i} -> {el} -> {config[i]}")
    else:
        move = line.strip()
        search = re.search('move (.*) from (.*) to (.*)', line)
        if search is not None:
            qty = int(search.group(1))
            fromIndex = int(search.group(2))
            toIndex = int(search.group(3))
            print(f"Moving {qty} boxes from {fromIndex} to {toIndex}")
            for box in range(0, qty):
                removed = config[fromIndex-1].pop()
                config[toIndex-1].append(removed)

solution = ""
for i in range(0, N):
    solution += config[i].pop()

print(solution)
