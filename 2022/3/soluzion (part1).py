import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\input.txt', 'r')
Lines = file1.readlines()
charList = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

total = 0

for line in Lines:
    text = line.strip()
    size = len(text)
    half = int(size/2)
    firstPart = text[0:half]
    secondPart = text[half:]
    commonChars = set(list(firstPart)) & set(list(secondPart))
    commonChar = commonChars.pop()
    charValue = charList.index(commonChar) + 1
    total += charValue
    print(f"{firstPart} / {secondPart} -> {commonChar} -> {charValue}")

print(f"TOTAL -> {total}")