with open("input", "r") as f:
	lines = f.readlines()
register = []

for line in lines:
	line = line.strip().split(" ")
	register.append(register[-1] if len(register) > 0 else 1)
	if line[0] == "addx":
		register.append(register[-1] + int(line[1]))

signalstrengths = []
for cycle in range(len(register)):
	signalstrengths.append((cycle + 1) * register[cycle])

print(signalstrengths[19]+signalstrengths[59]+signalstrengths[99]+signalstrengths[139]+signalstrengths[179]+signalstrengths[219])