with open("input", "r") as f:
	line = f.readline()
size = 4
while len(set(line[size-4:size])) < 4:
	size += 1
print(size)