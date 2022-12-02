input_file = open("input", "r")
lines = input_file.readlines()
score = 0
for line in lines:
	opponent = ord(line[0]) - ord('A')
	win = 3 * (ord(line[2]) - ord('X'))
	you = opponent
	if (win == 0):
		you = ((opponent + 2) % 3)
	if (win == 6):
		you = ((opponent + 1) % 3)
	score += 1 + you + win
print(score)
input_file.close()