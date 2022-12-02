input_file = open("input", "r")
lines = input_file.readlines()
score = 0
for line in lines:
	opponent = ord(line[0]) - ord('A')
	you = ord(line[2]) - ord('X')
	win = 0
	if (opponent == you):
		win = 3
	if (opponent == ((you + 2) % 3)):
		win = 6
	score += 1 + you + win
print(score)
input_file.close()