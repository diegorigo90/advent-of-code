import os
import re
import random

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input2.txt', "r")
lines = f.readlines()


class Info:
    def __init__(self, _flow_rate, _valves):
        self.flow_rate = _flow_rate
        self.valves = _valves


info = {}

for line in lines:
    text = line.strip()
    match = re.match("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", text)
    valve = match.group(1)
    flow_rate = int(match.group(2))
    valves = [s.strip() for s in match.group(3).split(",")]
    info[valve] = Info(flow_rate, valves)

max_value = 0
for index in range(0, 1000000):
    position = "AA"
    visited = set()
    visited.add(position)
    to_continue = True
    i = 0
    opened_valves = []
    path = [position]
    value = 0

    while i < 30:
        for opened_valve in opened_valves:
            value += info[opened_valve].flow_rate
        curr_info = info[position]
        flow_rate = curr_info.flow_rate
        next_positions = curr_info.valves
        next_position = random.choice(next_positions)
        path.append(next_position)
        dice = random.choice([True, False])
        if dice and position not in opened_valves:
            # Open valve (one round lost)
            i += 1
            opened_valves.append(position)
        # print(f"Moving from {position} to {next_position}")
        visited.add(next_position)
        position = next_position
        i += 1
        if len(visited) == len(info):
            break

    if value > max_value:
        max_value = value
        print(f"New max value: {max_value}")
    if (index % 10000) == 0:
        print(index)

print(f"Max value: {max_value}")
