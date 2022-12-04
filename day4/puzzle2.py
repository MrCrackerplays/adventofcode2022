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
	if first[0] <= second[0] <= first[1] or second[0] <= first[0] <= second[1]:
		overlaps += 1
print(overlaps)
input_file.close()