import os
import re
from treelib import Tree
import sys

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\\input.txt', "r")
line = f.readline().strip()
tree = Tree()
currentNode = None

while True:
    if line == "":
        break
    changeDir = re.search('\$ cd (.*)', line)
    if line == "$ cd /":
        tree.create_node("home", "home", currentNode, {"type": "directory"})
        currentNode = tree.get_node("home")
        line = f.readline().strip()
    elif line == '$ cd ..':
        currentNode = tree.get_node(currentNode.predecessor(tree.identifier))
        size = 0
        line = f.readline().strip()
    elif changeDir is not None:
        my_dir = changeDir.group(1)
        name = currentNode.identifier + "/" + my_dir
        currentNode = tree.get_node(name)
        line = f.readline().strip()
    elif line == '$ ls':
        while True:
            line = f.readline().strip()
            directory = re.search("dir (.*)", line)
            file = re.search("(.*\d) (.*\w)", line)
            if directory is not None:
                my_dir = directory.group(1)
                name = currentNode.identifier + "/" + my_dir
                tree.create_node(my_dir, name, currentNode, {"type": "directory"})
            elif file is not None:
                filename = file.group(2)
                size = int(file.group(1))
                name = currentNode.identifier + "/" + filename
                tree.create_node(filename, name, currentNode, {"type": "file", "size": size})
            else:
                break
    else:
        line = f.readline().strip()


def compute_size(_node):
    _size = 0
    _type = _node.data.get("type")
    if _type == "directory":
        for child in _node.successors(tree.identifier):
            _size += compute_size(tree.get_node(child))
    else:
        _size += _node.data.get("size")
    _node.data = {"type": _type, "size": _size}
    return _size


compute_size(tree.get_node("home"))

# spazio totale
root = tree.get_node("home")
size = root.data.get("size")
print(f"Spazio occupato attualmente: {size}")

# spazio inutilizzato
inutilizzato = 70000000 - size
print(f"Spazio inutilizzato attualmente: {inutilizzato}")

# spazio da liberare
daLiberare = 30000000 - inutilizzato
print(f"Spazio da liberare: {daLiberare}")

# trovo la directory minima con spazio maggiore dello spazio da liberare
m = sys.maxsize
for node in tree.all_nodes_itr():
    type = node.data.get("type")
    size = node.data.get("size")
    if type == "directory" and size >= daLiberare:
        m = min(m, size)

print(f"MINIMO: {m}")
