import os
import multiprocessing
from functools import partial
from contextlib import contextmanager

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()

monkeys = {}
values = {}

for line in lines:
    text = line.strip()
    [name, operation] = text.split(": ")
    monkeys[name] = operation


def get_value(_name, _val):
    _operation = monkeys[_name]
    if _name == 'humn':
        value = _val
    elif _name == 'root':
        # print(f"Computing {_name}/{_val}")
        [a, b] = _operation.split(" + ")
        value = get_value(a, _val) == get_value(b, _val)
    elif _name in values:
        value = values[_name]
    else:
        if " + " in _operation:
            [a, b] = _operation.split(" + ")
            value = get_value(a, _val) + get_value(b, _val)
        elif " - " in _operation:
            [a, b] = _operation.split(" - ")
            value = get_value(a, _val) - get_value(b, _val)
        elif " * " in _operation:
            [a, b] = _operation.split(" * ")
            value = get_value(a, _val) * get_value(b, _val)
        elif " / " in _operation:
            [a, b] = _operation.split(" / ")
            value = get_value(a, _val) / get_value(b, _val)
        else:
            value = int(_operation)

        values[_name] = value

    return value


arguments = [("root", x) for x in range(0, 100000)]

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        pool.starmap(get_value, arguments)
        print("END")
