input_file = open("input", "r")
lines = input_file.readlines()
elves = [0]
id = 0
for line in lines:
	if line.strip():
		elves[id] += int(line)
	else:
		elves.append(0)
		id += 1
print(sum(sorted(elves)[-3:]))
input_file.close()