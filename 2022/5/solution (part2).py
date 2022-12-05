import os
import re

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\input.txt', 'r')
Lines = file1.readlines()

topInfo = True
config = []
N = 9
for j in range(1,N+1):
    config.append([])

for line in Lines:
    if (" 1   2   3" in line):
        topInfo = False
        for i in range(0,len(config)):
            print(f"{config[i]}")

    if (topInfo):
        for i in range(0,N):
            el = line[1+4*i]
            if el.strip() != "":
                config[i].insert(0,el)
    else:
        move = line.strip()
        search = re.search('move (.*) from (.*) to (.*)', line)
        if search != None:    
            qty = int(search.group(1))
            fromIndex = int(search.group(2))
            toIndex = int(search.group(3))
            print(f"Moving {qty} boxes from {fromIndex} to {toIndex}")
            columnFrom = config[fromIndex-1]
            removed = columnFrom[len(columnFrom)-qty:]
            del columnFrom[len(columnFrom)-qty:]
            config[toIndex-1] += removed

solution = ""
for i in range(0,N):
    solution += config[i].pop()

print(solution)