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

checkrow = 2000000

not_present = set()
for k, v in sensors.items():
	dist = manhattan_distance(k, (k[0], checkrow))
	if dist > v:
		continue
	to_check = -2 * (dist - v) + 1
	for x in range(k[0] + (dist - v), k[0] + to_check + (dist - v)):
		if (x, checkrow) not in beacons:
			not_present.add((x, checkrow))
print(len(not_present))