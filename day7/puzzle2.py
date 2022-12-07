with open("input", "r") as f:
	lines = f.readlines()
current_dir = "/"
# folder_contents = {"/": {"a/": -1}, "/a/" : {"e/": -1, "a.txt": 1}, "/a/e/": {"e.txt": 2}}
folder_contents = {"/": {}}
# folder_sizes = {"/": 3, "/a/": 3, "/a/e/": 2}
folder_sizes = {}
for line in lines:
	line = line.strip().split(" ")
	if (line[0] == "$"):
		if line[1] == "cd":
			if line[2] == "/":
				current_dir = "/"
			elif line[2] == ".." and current_dir != "/":
				end = -1
				while current_dir[end - 1] != "/":
					end -= 1
				current_dir = current_dir[:end]
			else:
				current_dir += line[2] + "/"
				if current_dir not in folder_contents:
					folder_contents[current_dir] = {}
	else:
		if current_dir not in folder_contents:
			folder_contents[current_dir] = {}
		folder_contents[current_dir][line[1]] = -1 if line[0] == "dir" else int(line[0])
keylist = list(folder_contents.keys())
keylist.sort(key = len, reverse = True)
#sorting by longest directory paths means that it build the sizes from the subdirectories up
for folder in keylist:
	if folder not in folder_sizes:
		folder_sizes[folder] = 0
	for item in folder_contents[folder]:
		size = folder_contents[folder][item]
		if size < 0:
			#directory
			size = folder_sizes[folder + item + "/"]
		folder_sizes[folder] += size
available = 70000000 - folder_sizes["/"]
smallest = 70000000
for folder in folder_sizes:
	if folder_sizes[folder] > (30000000 - available) and folder_sizes[folder] < smallest:
		smallest = folder_sizes[folder]
print(smallest)