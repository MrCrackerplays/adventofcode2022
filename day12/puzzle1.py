with open("input", "r") as f:
	lines = f.readlines()

def find_directionality(x, y):
	directions = 0
	if x > 0 and ord(lines[y][x-1]) <= ord(lines[y][x]) + 1:
		directions |= 0b0001
	if x < len(lines[y])-1 and ord(lines[y][x+1]) <= ord(lines[y][x]) + 1:
		directions |= 0b0010
	if y > 0 and ord(lines[y-1][x]) <= ord(lines[y][x]) + 1:
		directions |= 0b0100
	if y < len(lines)-1 and ord(lines[y+1][x]) <= ord(lines[y][x]) + 1:
		directions |= 0b1000
	return directions

directional_map = []
for y in range(len(lines)):
	lines[y] = lines[y].strip()
	directional_map.append([])
	for x in range(len(lines[y])):
		if lines[y][x] == "S":
			start = (x, y)
			lines[y] = lines[y][:x] + "a" + lines[y][x+1:]
		elif lines[y][x] == "E":
			end = (x, y)
			lines[y] = lines[y][:x] + "z" + lines[y][x+1:]

for y in range(len(lines)):
	for x in range(len(lines[y])):
		directional_map[y].append(find_directionality(x, y))


#implementing A* using a tutorial

# let openList equal empty list of nodes
open_nodes = {}
# let closedList equal empty list of nodes
closed_nodes = {}
# put startNode on the openList (leave it's f at zero)
open_nodes[start] = {"g": 0, "h": 0, "f": 0}
# while openList is not empty
while len(open_nodes) > 0:
#     let currentNode equal the node with the least f value
	current_node_coordinates = list(open_nodes.keys())[0]
	current_node = open_nodes[current_node_coordinates]
	for coordinates,node in open_nodes.items():
		if node["f"] < current_node["f"]:
			current_node_coordinates = coordinates
			current_node = node
#     remove currentNode from the openList
	open_nodes.pop(current_node_coordinates)
#     add currentNode to the closedList
	closed_nodes[current_node_coordinates] = current_node
#     if currentNode is the goal
#         You've found the exit!
	if current_node_coordinates == end:
		break
#     let children of the currentNode equal the adjacent nodes
	children = []
	if directional_map[current_node_coordinates[1]][current_node_coordinates[0]] & 0b0001 != 0:
		children.append((current_node_coordinates[0]-1, current_node_coordinates[1]))
	if directional_map[current_node_coordinates[1]][current_node_coordinates[0]] & 0b0010 != 0:
		children.append((current_node_coordinates[0]+1, current_node_coordinates[1]))
	if directional_map[current_node_coordinates[1]][current_node_coordinates[0]] & 0b0100 != 0:
		children.append((current_node_coordinates[0], current_node_coordinates[1]-1))
	if directional_map[current_node_coordinates[1]][current_node_coordinates[0]] & 0b1000 != 0:
		children.append((current_node_coordinates[0], current_node_coordinates[1]+1))
#     for each child in the children
	for child in children:
#         if child is in the closedList
		if child in closed_nodes:
#             continue to beginning of for loop
			continue
#         child.g = currentNode.g + distance b/w child and current
		new_node = {"g": current_node["g"]+1}
#         child.h = distance from child to end
		new_node["h"] = abs(child[0]-end[0]) + abs(child[1]-end[1])
#         child.f = child.g + child.h
		new_node["f"] = new_node["g"] + new_node["h"]
#         if child.position is in the openList's nodes positions
		if child in open_nodes:
#             if child.g is higher than the openList node's g
			if new_node["g"] > open_nodes[child]["g"]:
#                 continue to beginning of for loop
				continue
#         add the child to the openList
		open_nodes[child] = new_node

print(closed_nodes[end]["f"])