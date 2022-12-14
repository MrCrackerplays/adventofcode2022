with open("input", "r") as f:
	lines = f.readlines()

positions = set()

for line in lines:
	line = line.strip().split(" -> ")
	previous = None
	for i in range(len(line)):
		line[i] = line[i].split(",")
		line[i][0] = int(line[i][0])
		line[i][1] = int(line[i][1])
		current = line[i]
		if previous == None:
			previous = current
		while previous != current:
			positions.add((previous[0], previous[1]))
			if current[0] != previous[0]:
				previous[0] += (current[0] - previous[0]) / abs(current[0] - previous[0])
			if current[1] != previous[1]:
				previous[1] += (current[1] - previous[1]) / abs(current[1] - previous[1])
		positions.add((previous[0], previous[1]))

#[top left corner, bottom right corner]
bounds = [[500, 0], [500, 0]]
for key in positions:
	if key[0] < bounds[0][0]:
		bounds[0][0] = key[0]
	if key[1] < bounds[0][1]:
		bounds[0][1] = key[1]
	if key[0] > bounds[1][0]:
		bounds[1][0] = key[0]
	if key[1] > bounds[1][1]:
		bounds[1][1] = key[1]

floorheight = bounds[1][1] + 2
floorwidth = floorheight * 2 + 1
for x in range(-floorheight, floorwidth - floorheight):
	positions.add((500 + x, floorheight))
if 500 - floorheight < bounds[0][0]:
	bounds[0][0] = 500 - floorheight
if 500 + floorheight > bounds[1][0]:
	bounds[1][0] = 500 + floorheight
bounds[1][1] += 2

previous_grains = -1
grains = 0
while previous_grains != grains:
	previous_grains = grains
	oldx = 500
	oldy = -1
	x = 500
	y = 0
	while (x, y) != (oldx, oldy) and bounds[0][0] <= x and x <= bounds[1][0] and bounds[1][1] > y:
		oldx = x
		oldy = y
		if (x, y + 1) not in positions:
			y += 1
		elif (x - 1, y + 1) not in positions:
			y += 1
			x -= 1
		elif (x + 1, y + 1) not in positions:
			y += 1
			x += 1
	if bounds[0][0] <= x and x <= bounds[1][0] and bounds[1][1] > y and (x, y) not in positions:
		positions.add((x, y))
		grains += 1
print(grains)