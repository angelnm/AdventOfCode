MOVES = [[+0, +1],[+1, +0],[+0, -1],[-1, +0]]

def read_file(nameFile):
	file = open(nameFile, 'r')

	c_map = []
	start = []
	end = []
	for y, row in enumerate(file):
		c_row = []
		for x, data in enumerate(row.rstrip()):
			if data == "S":
				start = [x, y]
				data = '.'
			elif data == "E":
				end = [x, y]
				data = '.'
			c_row.append(data)
		c_map.append(c_row)

	c_run = [start]
	while True:
		c_pos = c_run[-1]

		c_x = c_pos[0]
		c_y = c_pos[1]
		c_map[c_y][c_x] = len(c_run)-1

		added = False
		for m in MOVES:
			x = c_x + m[0]
			y = c_y + m[1]

			if c_map[y][x] == '.':
				c_run.append ([x,y])
				added = True
				
		if not added:
			break


	return c_map, c_run

def cheating_run(c_map, c_run):
	cheated = {}
	cheat_dist = 20
	min_gained = 0
	for dist1, pos1 in enumerate(c_run):
		for dist2, pos2 in enumerate(c_run[dist1+1:]):
			dist2 += dist1+1 

			compute_dist  = abs(pos1[0]-pos2[0])
			compute_dist += abs(pos1[1]-pos2[1])

			if compute_dist > cheat_dist:
				continue

			saved_dist = dist2 - dist1
			if saved_dist <= compute_dist:
				continue

			saved_dist -= compute_dist
			if saved_dist not in cheated:
				cheated[saved_dist] = 0
			cheated[saved_dist]+=1

	print(cheated)
	total = 0
	for key in cheated:
		if key >= 100:
			total += cheated[key]
			print(key, cheated[key])
	print(total)

def main():
	c_map, c_run = read_file('input2.txt')

	cheating_run(c_map, c_run)

	"""
	for c_row in c_map:
		string = ""
		for data in c_row:
			if len(str(data)) == 1:
				string += " "
			string += " "+str(data)
		print(string, sep="")
	"""

main()