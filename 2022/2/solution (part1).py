import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(location + '\input.txt', 'r')
Lines = file1.readlines()

map1 = {
    "A": 1,
    "B": 2,
    "C": 3
}
map2 = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

matrix=[
    [3,6,0],
    [0,3,6],
    [6,0,3]
]

points = 0

for line in Lines:
    i = map1.get(line[0])
    j = map2.get(line[2])
    victoryPoints = matrix[i-1][j-1]

    matchPoints = j + victoryPoints
    points += matchPoints
    print(f"Values {i}/{j} -> {victoryPoints}")

print(f"TOTAL POINTS: {points}")