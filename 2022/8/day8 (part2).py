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


def count_lowers(_el, _list):
    _count = 0
    for _val in _list:
        if _val < _el:
            _count = _count + 1
        else:
            _count = _count + 1
            break
    return _count


M = np.asarray(my_list)
count = 0
maxVal = -1
for i in range(0, rows):
    for j in range(0, cols):
        el = M[i][j]
        a = count_lowers(el, np.flip(M[i, 0:j]))
        b = count_lowers(el, M[i, j + 1:])
        c = count_lowers(el, np.flip(M[0:i, j]))
        d = count_lowers(el, M[i + 1:, j])
        val = a * b * c * d
        if val > maxVal:
            maxVal = val
print(maxVal)
