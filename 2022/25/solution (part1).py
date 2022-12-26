import os
import random

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()


def get_value(_text):
    _result = 0
    for _i in range(0, len(_text)):
        _number = _text[len(_text) - _i - 1]
        if _number == "=":
            _number = -2
        elif _number == "-":
            _number = -1
        else:
            _number = int(_number)
        _result += _number * (5 ** _i)
    return _result


total = 0
for line in lines:
    text = line.strip()
    value = get_value(text)
    total += value
    # print(f"{text} -> {value}")

print(f"TOTAL: {total}")

test = "="

chars = ["=", "-", "0", "1", "2"]


def get_next_char(_char):
    next_char = None
    if _char in chars:
        index = chars.index(_char)
        if index + 1 <= len(chars) - 1:
            next_char = chars[index + 1]
    return next_char


def add_one(_string):
    last_char = _string[len(_string) - 1]
    next_char = get_next_char(last_char)
    result = [*_string]
    if next_char is not None:
        result[len(result) - 1] = next_char
    else:
        last_char = "="
        index = len(_string) - 1
        sub = _string[0:index]
        if len(sub) > 0:
            substring = add_one(sub)
            result = [substring, last_char]
        else:
            result = ["="]
            result.extend(["="] * len(_string))
    return ''.join(result)


value = ""
for i in range(0, 20):
    value += "1"
    decimal_value = get_value(value)
    if decimal_value > total:
        value = value[0:len(value) - 1]
print(f"{value} -> {get_value(value)}")


for i in range(0, 4000000):
    test_string = [random.choice(chars) for j in value]
    test_string = "".join(test_string)
    test_value = get_value(test_string)
    if i % 10000 == 0:
        print(f"Checking for new best value: {test_string}")
    if get_value(value) < test_value <= total:
        value = test_string
        print(f"Found new best value: {test_string} -> {test_value} (Distance {total - test_value})")

count = 0
while True:
    next_value = add_one(value)
    value = next_value
    decimal_value = get_value(value)
    if decimal_value == total:
        print(f"TROVATO: {value} -> {decimal_value}")
        break
    count += 1
    if count > 0 and count % 100000 == 0:
        print(f"TESTING {value} -> {decimal_value} (Distance {total - decimal_value})")
