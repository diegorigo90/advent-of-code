import os
import re
from treelib import Tree

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(location + '\input.txt',"r")
line = f.readline().strip()
tree = Tree()
currentNode = None

while True:
    if line == "":
        break
    changeDir = re.search('\$ cd (.*)', line)
    if line == "$ cd /":
        tree.create_node("home","home",currentNode, {"type":"directory"})
        currentNode = tree.get_node("home")
        line = f.readline().strip()
    elif line == '$ cd ..':
        currentNode = tree.get_node(currentNode.predecessor(tree.identifier))
        size = 0
        line = f.readline().strip()
    elif changeDir is not None:
        dir = changeDir.group(1)
        name = currentNode.identifier + "/" + dir
        currentNode = tree.get_node(name)
        line = f.readline().strip()
    elif line == '$ ls':
        while True:
            line = f.readline().strip()
            directory = re.search("dir (.*)",line)
            file = re.search("(.*\d) (.*\w)",line)
            if directory is not None:
                dir = directory.group(1)
                name = currentNode.identifier + "/" + dir
                tree.create_node(dir,name,currentNode,{"type": "directory"})
            elif file is not None:
                filename = file.group(2)
                size = int(file.group(1))
                name = currentNode.identifier + "/" + filename
                tree.create_node(filename,name,currentNode,{"type": "file", "size": size})
            else:
                break
    else:
        line = f.readline().strip()


def computesize(node):
    size = 0
    type = node.data.get("type")
    if type == "directory":
        for child in node.successors(tree.identifier):
            size += computesize(tree.get_node(child))
    else:
        size += node.data.get("size")
    node.data = {"type": type, "size": size}
    return size

computesize(tree.get_node("home"))
        

sum = 0
for node in  tree.all_nodes_itr():
    type = node.data.get("type")
    size = node.data.get("size")
    if (type == "directory" and size <= 100000):
        sum += size
print("TOTALE: " + str(sum))
