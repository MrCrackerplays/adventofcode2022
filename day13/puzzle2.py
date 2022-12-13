with open("input", "r") as f:
	lines = f.readlines()

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
		if type(local_first[i]) == list or type(local_second[i]) == list:
			if type(local_first[i]) != type(local_second[i]):
				if type(local_first[i]) == int:
					comparison = compare_lists([local_first[i]], local_second[i])
				else:
					comparison = compare_lists(local_first[i], [local_second[i]])
			else:
				comparison = compare_lists(local_first[i], local_second[i])
		else:
			comparison = compare_ints(local_first[i], local_second[i])
		if comparison != 0:
			return comparison
	return 0

lists = []

for i in range(len(lines)):
	line = lines[i].strip()
	if line != "":
		lists.append(eval(line))
lists.append([[2]])
lists.append([[6]])

sorted_list = sorted(lists, cmp=compare_lists, reverse=True)

for i in range(len(sorted_list)):
	if sorted_list[i] == [[2]]:
		first = i + 1
	elif sorted_list[i] == [[6]]:
		second = i + 1
print(first * second)
