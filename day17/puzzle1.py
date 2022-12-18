with open("input", "r") as f:
	line = f.readline().strip()

iteration = 0

def get_direction():
	iteration = iteration % len(line)
	return line[iteration]

stones = [
	["####"],

	[".#.",
	 "###",
	 ".#."],

	["..#",
	 "..#",
	 "###"],
	
	["#",
	 "#",
	 "#",
	 "#"],
	
	["##",
	 "##"]
]

well = []
fallen_stones = 0
def stone_drop():
	stone = stones[-(1 + (fallen_stones % len(stones)))]
	# for i in range(3):
	# 	well.append(".......")
	bottom_left = [2, len(well)]
	for layer in stone:
		well.append(".......")
		well[-1] = well[-1][:bottom_left[0]] + layer + well[-1][bottom_left[0]+len(layer):]
	# moving = True
	# while moving:
	# 	if get_direction() == "<":
	# 		# move left
	# 		pass
	# 	else:
	# 		# move right
	# 		pass
	# 	iteration += 1
	# 	#move down

while fallen_stones < 10:
	stone_drop()
	fallen_stones += 1
for layer in well:
	print(layer)