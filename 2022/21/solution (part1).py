import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()

monkeys = {}
values = {}


def get_value(_name):
    _operation = monkeys[_name]

    if _name in values:
        return values[_name]
    else:
        if " + " in _operation:
            [a, b] = _operation.split(" + ")
            value = get_value(a) + get_value(b)
        elif " - " in _operation:
            [a, b] = _operation.split(" - ")
            value = get_value(a) - get_value(b)
        elif " * " in _operation:
            [a, b] = _operation.split(" * ")
            value = get_value(a) * get_value(b)
        elif " / " in _operation:
            [a, b] = _operation.split(" / ")
            value = get_value(a) / get_value(b)
        else:
            value = int(_operation)

        values[_name] = value
        return value


for line in lines:
    text = line.strip()
    [name, operation] = text.split(": ")
    monkeys[name] = operation

val = get_value("root")
print(val)
