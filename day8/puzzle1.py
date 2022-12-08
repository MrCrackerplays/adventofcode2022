with open("input", "r") as f:
	lines = f.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].strip()
width = len(lines[0])
height = len(lines)
def check_cardinal(lines, x, y):
	left = True
	right = True
	up = True
	down = True
	locx = x
	locy = y
	while locx > 0:
		locx -= 1
		if int(lines[locy][locx]) >= int(lines[y][x]):
			left = False
			break
	locx = x
	locy = y
	while locx < width - 1:
		locx += 1
		if int(lines[locy][locx]) >= int(lines[y][x]):
			right = False
			break
	locx = x
	locy = y
	while locy > 0:
		locy -= 1
		if int(lines[locy][locx]) >= int(lines[y][x]):
			up = False
			break
	locx = x
	locy = y
	while locy < height - 1:
		locy += 1
		if int(lines[locy][locx]) >= int(lines[y][x]):
			down = False
			break
	return left or right or up or down
total = 0
for y in range(height):
	for x in range(width):
		if x == 0 or x == width - 1 or y == 0 or y == height - 1:
			total += 1
			continue
		if check_cardinal(lines, x, y):
			total += 1
print(total)