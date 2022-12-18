import os
import re

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\\input.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    text = line.strip()
    search = re.search('(.*)-(.*),(.*)-(.*)', text)
    A = [int(search.group(1)), int(search.group(2))]
    B = [int(search.group(3)), int(search.group(4))]
    A_contains_B = A[0] <= B[0] and A[1] >= B[1]
    B_contains_A = B[0] <= A[0] and B[1] >= A[1]
    if A_contains_B:
        print(f"{A[0]} - {A[1]} / {B[0]} - {B[1]} -> A contains B")
        count += 1
    elif B_contains_A:
        print(f"{A[0]} - {A[1]} / {B[0]} - {B[1]} -> B contains A")
        count += 1
    

print(f"TOTAL: {count}")
