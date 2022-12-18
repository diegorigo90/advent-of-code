import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\\input.txt', 'r')
Lines = file1.readlines()
val = 0
my_list = []
for line in Lines:
    if line.strip():
        val += int(line)
    else:
        my_list.append(val)
        val = 0
my_list.sort(reverse=True)

total = 0
for i in [0, 1, 2]:
    total += my_list[i]
print(total)
