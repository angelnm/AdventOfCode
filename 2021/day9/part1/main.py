def get_sum_lower_points(c_map):
	width = len(c_map[0])
	height = len(c_map)
	summ = 0

	for x in range(width):
		for y in range(height):
			c_height = c_map[y][x]

			if y>0:
				if c_map[y-1][x]<=c_height:
					continue
			if y<height-1:
				if c_map[y+1][x]<=c_height:
					continue
			if x>0:
				if c_map[y][x-1]<=c_height:
					continue
			if x<width-1:
				if c_map[y][x+1]<=c_height:
					continue
			summ += c_height+1
	print(summ)


if __name__ == '__main__':
	with open('input.txt') as file:
		lines = file.read().splitlines()
		height_map = []
		for line in lines:
			line = list(line)
			c_height = []
			for height in line:
				c_height.append(int(height))
			height_map.append(c_height)

	get_sum_lower_points(height_map)