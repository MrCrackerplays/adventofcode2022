with open("input", "r") as f:
	lines = f.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].strip()
width = len(lines[0])
height = len(lines)
total = 0
visible = []
for y in range(height):
	visible.append([])
	for x in range(width):
		visible[y].append(0)
numblines = []
for y in range(height):
	numblines.append([])
	for x in range(width):
		numblines[y].append(int(lines[y][x]))
lines = numblines
for y in range(height):
	for x in range(width):
		left = 0
		right = 0
		up = 0
		down = 0

		locx = x
		locy = y
		local = -1
		while locx > 0:
			locx -= 1
			local = lines[locy][locx]
			left += 1
			if lines[locy][locx] >= lines[y][x]:
				break

		locx = x
		locy = y
		local = -1
		while locx < width - 1:
			locx += 1
			local = lines[locy][locx]
			right += 1
			if lines[locy][locx] >= lines[y][x]:
				break

		locx = x
		locy = y
		local = -1
		while locy > 0:
			locy -= 1
			local = lines[locy][locx]
			up += 1
			if lines[locy][locx] >= lines[y][x]:
				break

		locx = x
		locy = y
		local = -1
		while locy < height - 1:
			locy += 1
			local = lines[locy][locx]
			down += 1
			if lines[locy][locx] >= lines[y][x]:
				break
		visible[y][x] = left * right * up * down

highest = 0
for y in range(height):
	for x in range(width):
		if visible[y][x] > highest:
			highest = visible[y][x]
print(highest)
