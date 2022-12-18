import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
i = 0
array = []
while True:
    c = f.read(1)
    i += 1
    if not c:
        print("End of file")
        break
    else:
        array.append(c)
        if i > 4:
            del array[0]
            count = len(set(array))
            print(f"Reading character: {c} -> {array} -> {count}")
            if count == 4:
                break

print(f"Characters processed: {i}")
