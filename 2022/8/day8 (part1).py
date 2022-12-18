import numpy as np

f = open("/storage/emulated/0/Python/Day 8/input.txt", "r")
lines = f.readlines()
my_list = []
cols = 0
rows = 0

for line in lines:
	row = [int(x) for x in line.strip()]
	cols = max(cols, len(row))
	rows += 1
	my_list.append(row)


def is_bigger(_el, _list):
	greater_elements = _list[np.where(_list >= _el)]
	return len(greater_elements) == 0


M = np.asarray(my_list)
count = 0
for i in range(0, rows):
	for j in range(0, cols):
		el = M[i][j]
		leftRow = M[i, 0:j]
		if is_bigger(el, M[i, 0:j]) or is_bigger(el, M[i, j + 1:]) or is_bigger(el, M[0:i, j]) or is_bigger(el, M[i + 1:, j]):
			count += 1

print(count)
