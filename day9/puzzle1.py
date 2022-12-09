with open("input", "r") as f:
	lines = f.readlines()
visited = set()
visited.add((0, 0))
h = [0, 0]
t = [0, 0]
def move(direction):
	if direction == "U":
		h[1] += 1
	elif direction == "D":
		h[1] -= 1
	elif direction == "L":
		h[0] -= 1
	elif direction == "R":
		h[0] += 1
	if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
		if abs(h[0] - t[0]) > 1 and h[1] == t[1]:
			t[0] += (1 if h[0] > t[0] else -1) * (abs(h[0] - t[0]) - 1)
		elif abs(h[1] - t[1]) > 1 and h[0] == t[0]:
			t[1] += (1 if h[1] > t[1] else -1) * (abs(h[1] - t[1]) - 1)
		elif abs(h[0] - t[0]) > 1:
			t[0] += (1 if h[0] > t[0] else -1) * (abs(h[0] - t[0]) - 1)
			t[1] += (1 if h[1] > t[1] else -1) * abs(h[1] - t[1])
		elif abs(h[1] - t[1]) > 1:
			t[1] += (1 if h[1] > t[1] else -1) * (abs(h[1] - t[1]) - 1)
			t[0] += (1 if h[0] > t[0] else -1) * abs(h[0] - t[0])
	visited.add((t[0], t[1]))

for line in lines:
	line = line.strip().split(" ")
	for i in range(int(line[1])):
		move(line[0])
print(len(visited))