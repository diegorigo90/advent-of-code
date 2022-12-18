import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")


def compare(_line1, _line2):
    if type(_line1) is list and type(_line2) is list:
        length1 = len(_line1)
        length2 = len(_line2)
        for i in range(0, max(length1, length2)):
            if i >= length1:
                return True
            elif i >= length2:
                return False
            comparison = compare(_line1[i], _line2[i])
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


line1 = []
line2 = []
my_sum = 0
index = 0
while True:
    line = f.readline()
    if not line:
        break
    text = line.strip()
    if text != "":
        line1 = eval(text)
        text = f.readline().strip()
        line2 = eval(text)
        areEquals = compare(line1, line2)
        index += 1
        if areEquals:
            print(f"INDEX: {index} -> OK")
            my_sum += index
        else:
            print(f"INDEX: {index}")

print(f"SOMMA: {my_sum}")
