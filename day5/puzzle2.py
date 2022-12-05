with open("input", "r") as f:
	lines = f.readlines()
stacks = [[],[],[],[],[],[],[],[],[]]
arm_stack = []
stacks_filled = False
for line in lines:
	if not stacks_filled and line[1].isdigit():
		stacks_filled = True
		continue
	if not stacks_filled:
		index = 0
		while index < 9:
			if line[1 + (4 * index)] != " ":
				stacks[index].append(line[1 + (4 * index)])
			index += 1
		continue
	if line.strip() == "":
		continue
	#stacks are filled
	line = line.strip().split(" ")
	for _ in range(int(line[1])):
		arm_stack.insert(0, stacks[int(line[3]) - 1].pop(0))
	for _ in range(int(line[1])):
		stacks[int(line[5]) - 1].insert(0, arm_stack.pop(0))
print([item[0] for item in stacks])