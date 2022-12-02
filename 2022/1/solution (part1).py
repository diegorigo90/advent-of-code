import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\input.txt', 'r')
Lines = file1.readlines()
val = 0
maxVal = 0
for line in Lines:
    if line.strip():
        val += int(line)
    else:
        print(val)
        if val > maxVal:
            maxVal = val
        val = 0
print(val)
print("\n MAX VALUE: " + str(maxVal))