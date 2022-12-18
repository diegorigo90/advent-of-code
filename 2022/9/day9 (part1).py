import numpy as np

f = open("/storage/emulated/0/Python/input.txt", "r")

movements = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1])
}


def normalize(vector):
    x = vector[0]
    y = vector[1]
    if x != 0:
        x = x / abs(x)
    if y != 0:
        y = y / abs(y)
    return np.array([int(x), int(y)])


A = np.array([0, 0])
B = np.array([0, 0])
my_set = {str(B[0]) + str(B[1])}
lines = f.readlines()
for line in lines:
    text = line.strip()
    val = text.split(" ")
    direction = str(val[0])
    times = int(val[1])
    move = movements.get(val[0])
    val.append(move)
    for i in range(0, times):
        A = A + move
        dist = np.linalg.norm(B - A, ord=np.inf)
        if dist > 1:
            my_dir = A - B
            movement = normalize(my_dir)
            B = B + movement
            my_set.add(str(B[0]) + str(B[1]))
# print(str(dist) + " -> " + str(len(set)))
print(len(my_set))

f.close()
