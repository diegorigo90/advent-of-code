import os
import re
import networkx as nx
import matplotlib.pyplot as plt

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
lines = f.readlines()


class Info:
    def __init__(self, _valve, _flow_rate, _valves):
        self.valve = _valve
        self.flow_rate = _flow_rate
        self.valves = _valves


G = nx.Graph()
info = []

for line in lines:
    text = line.strip()
    match = re.match("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", text)
    valve = match.group(1)
    flow_rate = match.group(2)
    valves = [s.strip() for s in match.group(3).split(",")]
    info.append(Info(valve,flow_rate,valves))
    G.add_node(valve, rate=flow_rate, next=valves)

for node in info:
    for child in node.valves:
        G.add_edge(node.valve, child)
nx.draw(G, with_labels=True, node_size=800, node_color="#b95e0f", alpha=0.9, edge_color="#eac97a", font_color="#ffffff")
plt.show()
