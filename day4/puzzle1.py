#stackoverflow, I for the life of me couldn't think of how to find a total overlap I blame the time of release
def range_subset(range1, range2):
	"""Whether range1 is a subset of range2."""
	if not range1 or not range2:
		return True  # empty range is subset of anything
	if len(range1) > 1 and range1.step % range2.step:
		return False  # must have a single value or integer multiple step
	return range1.start in range2 and range1[-1] in range2


input_file = open("input", "r")
lines = input_file.readlines()
overlaps = 0
for line in lines:
	line = line.split(",")
	first = line[0].split("-")
	second = line[1].split("-")
	first[0] = int(first[0])
	first[1] = int(first[1])
	second[0] = int(second[0])
	second[1] = int(second[1])
	if range_subset(range(first[0], first[1] + 1), range(second[0], second[1] + 1)) or range_subset(range(second[0], second[1] + 1), range(first[0], first[1] + 1)):
		overlaps += 1
print(overlaps)
input_file.close()