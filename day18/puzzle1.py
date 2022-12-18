with open("input", "r") as f:
	lines = f.readlines()

points = set()

for line in lines:
	line = line.strip().split(",")
	points.add((int(line[0]), int(line[1]), int(line[2])))

covered = []

#X,Y,Z
#RIGHT:X+1 LEFT:X
#UP:Y+1 DOWN:Y
#FORWARD:Z+1 BACKWARD:Z

for (x, y, z) in points:
	if (x - 1, y, z) in points:
		#LEFT
		covered.append((x, y, z))
	if (x, y - 1, z) in points:
		#DOWN
		covered.append((x, y, z))
	if (x, y, z - 1) in points:
		#BACKWARD
		covered.append((x, y, z))

hidden = 2 * len(covered)
print((6 * len(points)) - hidden)
