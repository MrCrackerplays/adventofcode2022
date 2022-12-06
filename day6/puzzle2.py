with open("input", "r") as f:
	line = f.readline()
size = 14
while len(set(line[size-14:size])) < 14:
	size += 1
print(size)