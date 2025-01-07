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

	length = 0
	next_pos = start
	while next_pos != None:
		c_x = next_pos[0]
		c_y = next_pos[1]
		c_map[c_y][c_x] = length
		length += 1

		np = None
		for m in MOVES:
			x = c_x + m[0]
			y = c_y + m[1]

			if c_map[y][x] == '.':
				np = [x, y]
				break
		next_pos = np


	return c_map, start, end

def cheating_run(c_map, start, end):
	cheated = {}

	next_pos = start
	while next_pos != None:
		c_x = next_pos[0]
		c_y = next_pos[1]
		c_length = c_map[c_y][c_x]

		np = None
		for m in MOVES:
			x = c_x + m[0]
			y = c_y + m[1]

			if c_map[y][x] == c_length +1:
				np = [x, y]

			x = c_x + m[0]*2
			y = c_y + m[1]*2
			if x<0 or x>=len(c_map[0]):
				continue
			if y<0 or y>=len(c_map):
				continue
			this_length = c_map[y][x]
			if this_length != '#' and this_length+1 < c_length-1:
				dif = c_length - this_length -2
				if dif not in cheated:
					cheated[dif] = 0
				cheated[dif] += 1
		next_pos = np

	print(cheated)
	total = 0
	for key in cheated:
		if key >= 100:
			total += cheated[key]
	print(total)

def main():
	c_map, start, end = read_file('input2.txt')
	
	cheating_run(c_map, start, end)

	print(start, end)
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