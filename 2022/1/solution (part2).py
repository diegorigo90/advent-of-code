import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\input.txt', 'r')
Lines = file1.readlines()
val = 0
list = []
for line in Lines:
    if line.strip():
        val += int(line)
    else:
        list.append(val)
        val = 0
list.sort(reverse=True)

total = 0
for i in [0,1,2]: 
    total += list[i]
print(total)