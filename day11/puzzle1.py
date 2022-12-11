with open("input", "r") as f:
	lines = f.readlines()
monkeys = []

for i in range(len(lines)):
	line = lines[i].strip()
	if i % 7 == 0:
		monkeys.append({})
		monkeys[-1]["inspections"] = 0
	if i % 7 == 1:
		line = line.split(" ")
		monkeys[-1]["items"] = []
		for j in range(2, len(line)):
			if line[j][-1] == ",":
				line[j] = line[j][:-1]
			monkeys[-1]["items"].append(int(line[j]))
	if i % 7 == 2:
		monkeys[-1]["operation"] = line[17:]
	if i % 7 == 3:
		line = line.split(" ")
		monkeys[-1]["divisable"] = int(line[-1])
	if i % 7 == 4:
		line = line.split(" ")
		monkeys[-1]["true divisible"] = int(line[-1])
	if i % 7 == 5:
		line = line.split(" ")
		monkeys[-1]["false divisible"] = int(line[-1])

for round in range(20):
	for monkey in monkeys:
		for i in range(len(monkey["items"])):
			monkey["inspections"] += 1
			old = monkey["items"][i]
			new = eval(monkey["operation"]) // 3
			if new % monkey["divisable"] == 0:
				monkeys[monkey["true divisible"]]["items"].append(new)
			else:
				monkeys[monkey["false divisible"]]["items"].append(new)
		monkey["items"] = []

top = []
for monkey in monkeys:
	top.append(monkey["inspections"])
top.sort(reverse=True)
print(top[0] * top[1])