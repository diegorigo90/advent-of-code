import os
import time

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\input.txt',"r")

def compare(line1, line2):
    if (type(line1) is list and type(line2) is list):
        length1 = len(line1)
        length2 = len(line2)
        for i in range(0,max(length1, length2)):
            if i >= length1:
                return True
            elif i >= length2:
                return False
            comparison = compare(line1[i],line2[i])
            if comparison == True:
                return True
            elif comparison == False:
                return False
    elif (type(line1) is int and type(line2) is int):
        if line1 < line2:
            return True
        elif line1 > line2:
            return False
        else:
            return None
    else:
        part1 = []
        part2 = []
        if type(line1) is int:
            part1.append(line1)
        else:
            part1 = line1
        if type(line2) is int:
            part2.append(line2)
        else:
            part2 = line2
        return compare(part1,part2)
    return None

line1 = []
line2 = []
sum = 0
index = 0
while True:
    line = f.readline()
    if not line:
        break
    text = line.strip()
    if text != "":
        line1 = eval(text)
        text = f.readline().strip()
        line2 = eval(text)
        areEquals = compare(line1, line2)
        index += 1
        if areEquals:
            print(f"INDEX: {index} -> OK" )
            sum += index
        else:
            print(f"INDEX: {index}")


print(f"SOMMA: {sum}")
