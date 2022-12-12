import numpy as np
import time
import math
import re

f=open("/storage/emulated/0/Python/Day 10/input.txt","r")

total = 0
checkCycles = [20,60,100,140,180,220]

cycle = 0
value = 1
operations = []
for line in f.readlines():
	text = line.strip()
	noop = re.search("noop", text)
	addx = re.search("addx (.*)", text)
	if noop != None:
		operations.append(0)
	elif addx != None:
		val = int(addx.group(1))
		operations.append(0)
		operations.append(val)

screen = []
for i in range(0,6):
	line = []
	for j in range(0,40):
		line.append("")
	screen.append(line)

cycle = -1
for op in operations:
	cycle += 1
	txt = " "
	i = cycle // 40
	j = cycle % 40
	if j == value:
		txt = "#"
	print(f"{i}|{j} -> {txt}")
	screen[i][j] = txt
	value += op

for i in range(0,6):
	print("".join(screen[i]))