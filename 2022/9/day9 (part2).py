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


points = []
for i in range(0, 10):
    points.append(np.array([0, 0]))
my_set = {str(points[9][0]) + str(points[9][1])}
lines = f.readlines()
for line in lines:
    text = line.strip()
    val = text.split(" ")
    direction = str(val[0])
    times = int(val[1])
    move = movements.get(val[0])
    for i in range(0, times):
        points[0] = points[0] + move
        distances = []
        for j in range(1, 10):
            A = points[j - 1]
            B = points[j]
            dist = np.linalg.norm(B - A, ord=np.inf)
            distances.append(dist)
            if dist > 1:
                my_dir = A - B
                movement = normalize(my_dir)
                points[j] = B + movement
        my_set.add(str(points[9][0]) + str(points[9][1]))

print(len(my_set))
f.close()
