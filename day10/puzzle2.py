with open("input", "r") as f:
	lines = f.readlines()
register = [1]

for line in lines:
	line = line.strip().split(" ")
	register.append(register[-1] if len(register) > 0 else 1)
	if line[0] == "addx":
		register.append(register[-1] + int(line[1]))

crt = []
crt.append([])

def generate_line(i):
	line = "."*40
	middle = register[i]
	left = middle - 1
	right = middle + 1
	if left >= 0 and left < 40:
		line = line[:left] + "#" + line[left+1:]
	if middle >= 0 and middle < 40:
		line = line[:middle] + "#" + line[middle+1:]
	if right >= 0 and right < 40:
		line = line[:right] + "#" + line[right+1:]
	return line

for i in range(len(register)):
	if (i // 40) > len(crt) - 1:
		crt.append([])
	line = generate_line(i)
	crt[i//40].append(line[i % 40])
print(register[40:80])
for line in crt:
	result = ''.join(c for c in line)
	print(result)