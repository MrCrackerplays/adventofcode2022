with open("input", "r") as f:
	lines = f.readlines()

first = None
second = None
results = []

def compare_ints(local_first, local_second):
	if local_first < local_second:
		return 1
	elif local_first > local_second:
		return -1
	return 0

def compare_lists(local_first, local_second):
	for i in range(max(len(local_first), len(local_second))):
		if i == len(local_first) and i < len(local_second):
			return 1
		if i == len(local_first) and i == len(local_second):
			return 0
		if i < len(local_first) and i == len(local_second):
			return -1
		if type(local_first[i]) != type(local_second[i]):
			if type(local_first[i]) == int:
				local_first[i] = [local_first[i]]
			else:
				local_second[i] = [local_second[i]]
		if type(local_first[i]) == int:
			comparison = compare_ints(local_first[i], local_second[i])
		else:
			comparison = compare_lists(local_first[i], local_second[i])
		if comparison != 0:
			return comparison
	return 0


for i in range(len(lines)):
	line = lines[i].strip()
	if i % 3 == 0:
		first = eval(line)
	elif i % 3 == 1:
		second = eval(line)
	if second == None:
		continue
	results.append(compare_lists(first, second))
	first = None
	second = None

total = 0
for i in range(len(results)):
	if results[i] == 1:
		total += i + 1
print(total)