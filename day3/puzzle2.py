input_file = open("input", "r")
lines = input_file.readlines()
sum = 0
group = []
for line in lines:
	group.append("".join(set(line.strip())))
	if (len(group) != 3):
		continue
	com_str = "".join(set.intersection(*map(set,group)))
	group = []
	if (com_str.isupper()):
		charnum = ord(com_str) - ord('A') + 26
	else:
		charnum = ord(com_str) - ord('a')
	sum += 1 + charnum
print(sum)
input_file.close()