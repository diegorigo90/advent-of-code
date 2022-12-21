import os
import re
import time

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
    flow_rate = match.group(2)
    valves = [s.strip() for s in match.group(3).split(",")]
    info[valve] = Info(flow_rate, valves)

first_element = "AA"
paths = [
    [first_element]
]
finish = False

visited = set()
visited.add(first_element)
i = 0
to_continue = True

while to_continue:
    i += 1
    new_paths = []
    for path in paths:
        last_element = path[-1]
        print(f"Visited: {len(visited)}/{len(info)}")
        if len(visited) == len(info):
            to_continue = False
        else:
            next_valves = info[last_element].valves
            for valve in next_valves:
                visited.add(valve)
                new_list = list(path)
                new_list.append(valve)
                new_paths.append(new_list)
    paths = new_paths

for path in paths:
    print(path)
