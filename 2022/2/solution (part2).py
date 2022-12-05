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

victoryMap = {
    "X": 0,
    "Y": 3,
    "Z": 6
}
matrix=[
    ["Z","X","Y"],
    ["X","Y","Z"],
    ["Y","Z","X"]
]

points = 0

for line in Lines:
    i = map1.get(line[0])
    j = map2.get(line[2])
    selectedItem = matrix[i-1][j-1]
    selectedItemPoints = map2.get(selectedItem)
    victoryPoints = victoryMap.get(line[2])

    matchPoints = selectedItemPoints + victoryPoints
    points += matchPoints
    print(f"Values {line[0]}/{line[2]} -> {selectedItem} -> {selectedItemPoints}/{victoryPoints}")

print(f"TOTAL POINTS: {points}")