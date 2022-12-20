class Node:
    def __init__(self, val, name, parent, is_dir):
        self.val = val
        self.name = name
        self.children = []
        self.parent = parent
        self.is_dir = is_dir
        self.child_vals = 0
    def add_child(self, val, name, parent, is_dir):
        self.children.append(Node(val, name, parent, is_dir))
    def find_child(self, name):
        for i in range(0, len(self.children)):
            if self.children[i].name == name:
                return i
    def print_tree(self, level=0):
        ret = '\t'*level+str(self.val)+' '+str(self.name)+'\n'
        for c in self.children:
            ret += c.print_tree(level+1)
        return ret

txt = open("input_day_7.txt").read().splitlines()

# Part 1
root = Node('dir', '/', None, True)
curr = root
for cmd in txt:
    if cmd[:4] == '$ cd':
        if cmd[5] == '/':
            curr = root
        elif cmd[5:7] == '..':
            curr = curr.parent
        else:
            idx = curr.find_child(cmd[5:])
            curr = curr.children[idx]
    elif cmd[:3] == 'dir':
        curr.add_child('dir', cmd[4:], curr, True)
    elif cmd[0].isdigit():
        file = cmd.split()
        curr.add_child(int(file[0]), file[1], curr, False)

def sum_children(curr):
    child_sum = 0
    for child in curr.children:
        if not child.is_dir:
            child_sum += child.val
        child_sum += sum_children(child)
    return child_sum

total = 0
nodes = [root]
while True:
    new_nodes = []
    if len(nodes) == 0:
        break
    for node in nodes:
        if node.is_dir and sum_children(node) < 100000:
            total += sum_children(node)
        if len(node.children) > 0:
            for child in node.children:
                new_nodes.append(child)
    nodes = new_nodes

print(total)

# Part 2
total_size = sum_children(root)
space_needed = 30000000 - (70000000 - total_size)

lst = []
nodes = [root]
while True:
    new_nodes = []
    if len(nodes) == 0:
        break
    for node in nodes:
        if node.is_dir and sum_children(node) >= space_needed:
            lst.append(sum_children(node))
        if len(node.children) > 0:
            for child in node.children:
                new_nodes.append(child)
    nodes = new_nodes

print(sorted(lst)[0])