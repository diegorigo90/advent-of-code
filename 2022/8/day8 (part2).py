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
	
def countLowers(el, L):
	count = 0
	for val in L:
		if val < el:
			count = count + 1
		else:
			count = count + 1
			break			
	return count

M = np.asarray(list)
count = 0
maxVal = -1
for i in range(0, rows):
	for j in range(0,cols):
		el = M[i][j]
		a = countLowers(el, np.flip(M[i,0:j]))
		b = countLowers(el, M[i, j+1:])
		c = countLowers(el, np.flip(M[0:i, j]))
		d = countLowers(el, M[i+1:, j])
		val = a*b*c*d
		if val > maxVal:
			maxVal = val
print(maxVal)