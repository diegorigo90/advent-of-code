import os
import re

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\input.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    text = line.strip()
    search = re.search('(.*)-(.*),(.*)-(.*)', text)
    A = [int(search.group(1)), int(search.group(2))]
    B = [int(search.group(3)), int(search.group(4))]
    notOverlapped = B[0] > A[1] or B[1] < A[0]
    if (not notOverlapped):
        count += 1
    

print(f"TOTAL: {count}")
