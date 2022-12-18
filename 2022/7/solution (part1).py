import os
import re
from treelib import Tree

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
        dir1 = changeDir.group(1)
        name = currentNode.identifier + "/" + dir1
        currentNode = tree.get_node(name)
        line = f.readline().strip()
    elif line == '$ ls':
        while True:
            line = f.readline().strip()
            directory = re.search("dir (.*)", line)
            file = re.search("(.*\d) (.*\w)", line)
            if directory is not None:
                dir1 = directory.group(1)
                name = currentNode.identifier + "/" + dir1
                tree.create_node(dir1, name, currentNode, {"type": "directory"})
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

my_sum = 0
for node in tree.all_nodes_itr():
    _type = node.data.get("type")
    size = node.data.get("size")
    if _type == "directory" and size <= 100000:
        my_sum += size
print("TOTALE: " + str(my_sum))
