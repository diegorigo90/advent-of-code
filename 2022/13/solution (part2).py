import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")


def compare(_line1, _line2):
    if type(_line1) is list and type(_line2) is list:
        length1 = len(_line1)
        length2 = len(_line2)
        for _i in range(0, max(length1, length2)):
            if _i >= length1:
                return True
            elif _i >= length2:
                return False
            comparison = compare(_line1[_i], _line2[_i])
            if comparison:
                return True
            elif not comparison:
                return False
    elif type(_line1) is int and type(_line2) is int:
        if _line1 < _line2:
            return True
        elif _line1 > _line2:
            return False
        else:
            return None
    else:
        part1 = []
        part2 = []
        if type(_line1) is int:
            part1.append(_line1)
        else:
            part1 = _line1
        if type(_line2) is int:
            part2.append(_line2)
        else:
            part2 = _line2
        return compare(part1, part2)
    return None


lines = []
while True:
    line = f.readline()
    if not line:
        break
    text = line.strip()
    if text != "":
        lines.append(eval(text))

lines.append([[2]])
lines.append([[6]])


def bubble_sort(array):
    n = len(array)
    for _i in range(n):
        already_sorted = True
        for j in range(n - _i - 1):
            if not compare(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array


lines_sorted = bubble_sort(lines)
i = 0
val = 1
for line in lines_sorted:
    i += 1
    if line == [[2]] or line == [[6]]:
        val *= i

print(f"VALUE: {val}")
