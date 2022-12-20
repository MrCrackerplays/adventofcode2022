with open("input", "r") as f:
	input = f.readlines()

positions = []
for i in range(len(input)):
	input[i] = int(input[i].strip())
	positions.append(i)

def safe(pos):
	if pos == 0:
		return 0
	return pos % ((len(positions) - 1) * (pos / abs(pos)))

for i in range(len(positions)):
	position = positions.index(i)
	value = input[position]
	if value == 0:
		continue
	safepos = safe(position + value)
	positions.insert(safepos, positions.pop(position))
	input.insert(safepos, input.pop(position))
	if safepos == 0:
		positions = positions[1:] + positions[:1]
		input = input[1:] + input[:1]

thousand = (input.index(0) + 1000) % len(input)
twothousand = (input.index(0) + 2000) % len(input)
threesousand = (input.index(0) + 3000) % len(input)

sumtotal = input[thousand] + input[twothousand] + input[threesousand]
print(sumtotal)
