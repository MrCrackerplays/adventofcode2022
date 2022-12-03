input_file = open("input", "r")
lines = input_file.readlines()
sum = 0
for line in lines:
	n = len(line)
	string1 = line[0:n//2]
	string2 = line[n//2:]
	com_str = ''.join(set(string1).intersection(string2))
	if (com_str.isupper()):
		charnum = ord(com_str) - ord('A') + 26
	else:
		charnum = ord(com_str) - ord('a')
	sum += 1 + charnum
print(sum)
input_file.close()