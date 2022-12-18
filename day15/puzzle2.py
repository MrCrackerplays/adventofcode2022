with open("input", "r") as f:
	lines = f.readlines()

sensors = {}
beacons = set()

def manhattan_distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for line in lines:
	line = line[10:].strip().split(": closest beacon is at ")
	sensor = line[0].split(", ")
	sensor = (int(sensor[0][2:]), int(sensor[1][2:]))
	beacon = line[1].split(", ")
	beacon = (int(beacon[0][2:]), int(beacon[1][2:]))
	beacons.add(beacon)
	sensors[sensor] = manhattan_distance(sensor, beacon)

search_area = 4000000
ranges = []

def fix_overlaps(row):
	new_row = []
	actions = 0
	for r in row:
		if len(new_row) == 0:
			new_row.append(r)
			continue
		merged = False
		for n in new_row:
			if r[0] < n[0] and n[0] <= r[1] - 1:
				print("should never print")
				n[0] = r[0]
				merged = True
				actions += 1
			if r[0] <= 1 + n[1] and n[1] <= r[1]:
				n[1] = r[1]
				merged = True
				actions += 1
			if r[0] >= n[0] and r[1] <= n[1]:
				merged = True
				break
		if not merged:
			new_row.append(r)

	return (new_row, actions)

def merge_range(y, sensor, diff):
	local_range = [sensor[0] - diff, sensor[0] + diff]
	if local_range[1] < 0 or local_range[0] > search_area:
		return
	if local_range[0] < 0:
		local_range[0] = 0
	if local_range[1] > search_area:
		local_range[1] = search_area
	ranges[y].append(local_range)
	result = fix_overlaps(sorted(ranges[y]))
	while result[1] > 0:
		result = fix_overlaps(sorted(result[0]))
	ranges[y] = result[0]

goal = (0, 0)

for y in range(0, search_area):
	ranges.append([])
	for sensor, distance in sensors.items():
		diff = manhattan_distance(sensor, (sensor[0], y))
		if diff <= distance:
			merge_range(y, sensor, distance - diff)
	if len(ranges[y]) > 1:
		goal = (ranges[y][0][1] + 1, y)

print(goal, "=", 4000000 * goal[0] + goal[1])