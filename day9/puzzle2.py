with open("input", "r") as f:
	lines = f.readlines()
visited = set()
visited.add((0, 0))
knots = 10
knot_positions = [[0, 0] for i in range(knots)]
def move(direction):
	if direction == "U":
		knot_positions[0][1] += 1
	elif direction == "D":
		knot_positions[0][1] -= 1
	elif direction == "L":
		knot_positions[0][0] -= 1
	elif direction == "R":
		knot_positions[0][0] += 1

	for i in range(knots - 1):
		if abs(knot_positions[i][0] - knot_positions[i + 1][0]) > 1 or abs(knot_positions[i][1] - knot_positions[i + 1][1]) > 1:
			if abs(knot_positions[i][0] - knot_positions[i + 1][0]) > 1 and knot_positions[i][1] == knot_positions[i + 1][1]:
				knot_positions[i + 1][0] += (1 if knot_positions[i][0] > knot_positions[i + 1][0] else -1) * (abs(knot_positions[i][0] - knot_positions[i + 1][0]) - 1)
			elif abs(knot_positions[i][1] - knot_positions[i + 1][1]) > 1 and knot_positions[i][0] == knot_positions[i + 1][0]:
				knot_positions[i + 1][1] += (1 if knot_positions[i][1] > knot_positions[i + 1][1] else -1) * (abs(knot_positions[i][1] - knot_positions[i + 1][1]) - 1)
			elif abs(knot_positions[i][0] - knot_positions[i + 1][0]) > 1 and abs(knot_positions[i][1] - knot_positions[i + 1][1]) == 1:
				knot_positions[i + 1][0] += (1 if knot_positions[i][0] > knot_positions[i + 1][0] else -1) * (abs(knot_positions[i][0] - knot_positions[i + 1][0]) - 1)
				knot_positions[i + 1][1] += (1 if knot_positions[i][1] > knot_positions[i + 1][1] else -1) * abs(knot_positions[i][1] - knot_positions[i + 1][1])
			elif abs(knot_positions[i][1] - knot_positions[i + 1][1]) > 1 and abs(knot_positions[i][0] - knot_positions[i + 1][0]) == 1:
				knot_positions[i + 1][1] += (1 if knot_positions[i][1] > knot_positions[i + 1][1] else -1) * (abs(knot_positions[i][1] - knot_positions[i + 1][1]) - 1)
				knot_positions[i + 1][0] += (1 if knot_positions[i][0] > knot_positions[i + 1][0] else -1) * abs(knot_positions[i][0] - knot_positions[i + 1][0])
			elif abs(knot_positions[i][0] - knot_positions[i + 1][0]) > 1:
				knot_positions[i + 1][0] += (1 if knot_positions[i][0] > knot_positions[i + 1][0] else -1) * (abs(knot_positions[i][0] - knot_positions[i + 1][0]) - 1)
				knot_positions[i + 1][1] += (1 if knot_positions[i][1] > knot_positions[i + 1][1] else -1) * (abs(knot_positions[i][1] - knot_positions[i + 1][1]) - 1)
			elif abs(knot_positions[i][1] - knot_positions[i + 1][1]) > 1:
				knot_positions[i + 1][1] += (1 if knot_positions[i][1] > knot_positions[i + 1][1] else -1) * (abs(knot_positions[i][1] - knot_positions[i + 1][1]) - 1)
				knot_positions[i + 1][0] += (1 if knot_positions[i][0] > knot_positions[i + 1][0] else -1) * (abs(knot_positions[i][0] - knot_positions[i + 1][0]) - 1)

	visited.add((knot_positions[knots - 1][0], knot_positions[knots - 1][1]))

for line in lines:
	line = line.strip().split(" ")
	for i in range(int(line[1])):
		move(line[0])
print(len(visited))