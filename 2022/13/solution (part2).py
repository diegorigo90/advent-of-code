import os
import time
import functools

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

lines = []
while True:
    line = f.readline()
    if not line:
        break
    text = line.strip()
    if text != "":
        lines.append(eval(text))

lines.append([[2]])
lines.append([[6]])

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if not compare(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array

sorted = bubble_sort(lines)
i = 0
val = 1 
for line in sorted:
    i += 1
    if line ==  [[2]] or line == [[6]]:
        val *= i

print(f"VALUE: {val}")