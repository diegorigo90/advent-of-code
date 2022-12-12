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

for op in operations:
	cycle += 1
	strength = value * cycle
	if checkCycles.count(cycle) > 0:
		total += strength
		print(f"{cycle} ({op}): {value}/{strength}-> CHECK")
	else:
		print(f"{cycle} ({op}): {value}/{strength}")
	value += op

print(f"TOTAL: {total}")