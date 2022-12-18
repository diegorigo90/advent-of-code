import os
import re

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()

for line in lines:
    text = line.strip()
    match = re.match("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", text)
    valve = match.group(1)
    flow_rate = match.group(2)
    valves = [s.strip() for s in match.group(3).split(",")]
    print(f"{valve}: {flow_rate} -> {valves}")
