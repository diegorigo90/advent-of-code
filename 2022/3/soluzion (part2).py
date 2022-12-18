import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\\input.txt', 'r')
Lines = file1.readlines()
charList = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

total = 0
index = 0
strings = []

for line in Lines:
    index += 1
    if index == 3:
        strings.append(line.strip())
        commonChars = set(list(strings[0])) & set(list(strings[1])) & set(list(strings[2]))
        commonChar = commonChars.pop()
        charValue = charList.index(commonChar) + 1
        total += charValue
        print(f"{strings[0]} / {strings[1]} / {strings[2]} -> {commonChar} -> {charValue}")
        index = 0
        strings = []
    else:
        strings.append(line.strip())

print(f"TOTAL -> {total}")
