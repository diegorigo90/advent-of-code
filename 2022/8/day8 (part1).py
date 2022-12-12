import numpy as np
import time

f=open("/storage/emulated/0/Python/Day 8/input.txt","r")
lines = f.readlines()
list = []
cols = 0
rows = 0

for line in lines:
	row = [int(x) for x in line.strip()]
	cols = max(cols, len(row))
	rows += 1
	list.append(row)
	
def isbigger(el, L):
	greaterElements = L[np.where(L >= el)]
	return len(greaterElements) == 0

M = np.asarray(list)
count = 0
for i in range(0, rows):
	for j in range(0,cols):
		el = M[i][j]
		leftRow = M[i,0:j]
		if isbigger(el, M[i,0:j]) or isbigger(el, M[i, j+1:]) or isbigger(el, M[0:i, j]) or isbigger(el, M[i+1:, j]):
			count += 1

print(count)