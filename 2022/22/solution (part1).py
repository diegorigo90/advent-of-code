import os
import numpy

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()

info = []
instructions = []


def position_string(p):
    return "(" + str(p[1, 0]) + "," + str(p[0, 0]) + ")"


def get_instructions(_text):
    result = []
    val = ""
    for char in _text:
        if char.isdigit():
            val += char
        else:
            if result != "":
                result.append(val)
                val = ""
            result.append(char)
    return result


for line in lines:
    if line.strip() == "":
        continue
    elif "L" in line:
        instructions = get_instructions(line.strip())
    else:
        text = line.rstrip('\n')
        values = [*text]
        info.append(values)

n = len(max(info, key=len))
info_same_length = [x + [" "] * (n - len(x)) for x in info]
INFO = numpy.array(info_same_length)


def position_in_matrix(_position, _matrix):
    x = _position[0, 0]
    y = _position[1, 0]
    [_n, _m] = _matrix.shape
    return 0 <= x < _m and 0 <= y < _n


def get_value(_p):
    x = _p[0, 0]
    y = _p[1, 0]
    if position_in_matrix(_p, INFO):
        return INFO[y, x]
    else:
        return " "


p = numpy.array([[info[0].index(".")], [0]])
v = numpy.array([[1], [0]])
value = get_value(p)
rotation_matrix = numpy.array([[0, -1], [1, 0]])


def get_border_position(_p, _v):
    p1 = _p
    result_position = _p
    while True:
        p1 = p1 - _v
        _value = get_value(p1)
        if _value == " ":
            break
        else:
            if _value != " ":
                result_position = p1
    return result_position


print(f"Initial position: {position_string(p)}")
STORAGE = numpy.array(info_same_length)
STORAGE[p[1, 0], p[0, 0]] = "S"


def get_direction(_v):
    _v_x = _v[0,0]
    _v_y = _v[1, 0]
    result = ""
    if _v_x == 1 and _v_y == 0:
        result = ">"
    elif _v_x == -1 and _v_y == 0:
        result = "<"
    elif _v_x == 0 and _v_y == 1:
        result = "v"
    elif _v_x == 0 and _v_y == -1:
        result = "A"
    return result


for command in instructions:
    if command.isdigit():
        value = int(command)
        for i in range(0, value):
            p_new = p + v
            if get_value(p_new) == " ":
                print("Trovato fine mappa")
                border = get_border_position(p, v)
                if get_value(border) != "#":
                    p = border
                    direction = get_direction(v)
                    STORAGE[p[1, 0], p[0, 0]] = direction
            elif get_value(p_new) == "#":
                print("Trovato un muro")
                break
            else:
                p = p_new
                direction = get_direction(v)
                STORAGE[p[1, 0], p[0, 0]] = direction
                print("AVANTI DI 1")
            print(f"Position: {position_string(p)}")
    elif command == "R":
        v = rotation_matrix.dot(v)
        direction = get_direction(v)
        STORAGE[p[1, 0], p[0, 0]] = direction
        print(f"RUOTA IN SENSO ORARIO -> nuova direzione: ({v[0, 0]}, {v[1, 0]})")
    else:
        v = -rotation_matrix.dot(v)
        direction = get_direction(v)
        STORAGE[p[1, 0], p[0, 0]] = direction
        print(f"RUOTA IN SENSO ANTIORARIO -> nuova direzione: ({v[0, 0]}, {v[1, 0]})")

direction = 0
v_x = v[0, 0]
v_y = v[1, 0]
if get_direction(v) == ">":
    direction = 0
elif get_direction(v) == "v":
    direction = 1
elif get_direction(v) == "<":
    direction = 2
elif get_direction(v) == "A":
    direction = 3

print(f"Final position: {position_string(p)}")
print(f"Direction: {get_direction(v)} -> {direction}")
result_value = 1000 * (p[1, 0] + 1) + 4 * (p[0, 0] + 1) + direction

_list = STORAGE.tolist()
numpy.savetxt("GFG.csv",
           _list,
           delimiter ="",
           fmt='% s')
