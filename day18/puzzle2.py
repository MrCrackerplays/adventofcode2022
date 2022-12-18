with open("input", "r") as f:
	lines = f.readlines()

points = set()

for line in lines:
	line = line.strip().split(",")
	points.add((int(line[0]), int(line[1]), int(line[2])))

xmax = max(points, key=lambda x:x[0])[0] + 1
xmin = min(points, key=lambda x:x[0])[0] - 1
ymax = max(points, key=lambda x:x[1])[1] + 1
ymin = min(points, key=lambda x:x[1])[1] - 1
zmax = max(points, key=lambda x:x[2])[2] + 1
zmin = min(points, key=lambda x:x[2])[2] - 1

cooled = []

#X,Y,Z
#RIGHT:X+1 LEFT:X
#UP:Y+1 DOWN:Y
#FORWARD:Z+1 BACKWARD:Z

steam = set()
flood = [(xmin, ymin, zmin)]

def check_valid(cube, dx, dy, dz):
	if cube[0] + dx < xmin or cube[0] + dx > xmax:
		return False
	if cube[1] + dy < ymin or cube[1] + dy > ymax:
		return False
	if cube[2] + dz < zmin or cube[2] + dz > zmax:
		return False
	if (cube[0] + dx, cube[1] + dy, cube[2] + dz) in steam:
		return False
	if (cube[0] + dx, cube[1] + dy, cube[2] + dz) in flood:
		return False
	if (cube[0] + dx, cube[1] + dy, cube[2] + dz) in points:
		if dx == 1 or dy == 1 or dz == 1:
			cooled.append((cube[0], cube[1], cube[2]))
		elif dx == -1:
			cooled.append((cube[0] + 1, cube[1], cube[2]))
		elif dy == -1:
			cooled.append((cube[0], cube[1] + 1, cube[2]))
		elif dz == -1:
			cooled.append((cube[0], cube[1], cube[2] + 1))
		else:
			print("something went horribly wrong")
		return False
	return True

while len(flood) > 0:
	cube = flood.pop()
	steam.add(cube)

	if (check_valid(cube, 1, 0, 0)):
		flood.append((cube[0] + 1, cube[1], cube[2]))
	if (check_valid(cube, -1, 0, 0)):
		flood.append((cube[0] - 1, cube[1], cube[2]))
	if (check_valid(cube, 0, 1, 0)):
		flood.append((cube[0], cube[1] + 1, cube[2]))
	if (check_valid(cube, 0, -1, 0)):
		flood.append((cube[0], cube[1] - 1, cube[2]))
	if (check_valid(cube, 0, 0, 1)):
		flood.append((cube[0], cube[1], cube[2] + 1))
	if (check_valid(cube, 0, 0, -1)):
		flood.append((cube[0], cube[1], cube[2] - 1))

print(len(cooled))
