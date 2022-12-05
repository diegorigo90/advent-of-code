import os
import re

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\input.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    text = line.strip()
    search = re.search('(.*)-(.*),(.*)-(.*)', text)
    A = [search.group(1), search.group(2)]
    B = [search.group(3), search.group(4)]
    AcontainsB = A[0] <= B[0] and A[1] >= B[1]
    BcontainsA = B[0] <= A[0] and B[1] >= A[1]
    if (AcontainsB):
        print(f"{A[0]} - {A[1]} / {B[0]} - {B[1]} -> A contains B")
        count += 1
    elif (BcontainsA):
        print(f"{A[0]} - {A[1]} / {B[0]} - {B[1]} -> B contains A")
        count += 1
    

print(f"TOTAL: {count}")
