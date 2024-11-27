import math

with open("input.txt", "r") as file:
    s = file.read()


class Node:
    def __init__(self, elem, left, right):
        self.elem = elem
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.elem} = ({self.left},{self.right})"

s = s.split("\n\n")
lr = s[0]
map = s[1]
map = [m for m in map.split("\n") if len(m)]
nodes = []
for l in map:
    split = l.split(' = ')
    elem = split[0]
    sinks = split[1].replace("(", "").replace(")", "").split(", ")
    nodes.append(Node(elem, sinks[0], sinks[1]))

node_map = {n.elem: n for n in nodes}

i = 0
curr_nodes = [node_map[n] for n in node_map.keys() if n[-1] == 'A']
cadences = []
for i in range(len(curr_nodes)):
    curr = curr_nodes[i]
    j = 0
    while curr.elem[-1] != 'Z':
        dir = lr[j%len(lr)]
        if dir == 'L':
            curr = node_map[curr.left]
        else:
            curr = node_map[curr.right]
        j += 1
    cadences.append(j)
    i += 1


def lcd(a, b):
    return abs(a*b)//math.gcd(a, b)

def lcd_arr(n):
    if len(n) <= 1:
        return n
    curr = 1
    for m in n:
        curr = lcd(curr, m)
    return curr


print(f"total:{lcd_arr(cadences)}")



# while not all(c.elem[-1] == 'Z' for c in curr_nodes):
#     new_nodes = []
#     for curr in curr_nodes:
#         dir = lr[i%len(lr)]
#         if dir == 'L':
#             new_nodes.append(node_map[curr.left])
#         else:
#             new_nodes.append(node_map[curr.right])
#     i += 1
#     curr_nodes = new_nodes
# print(i)



