def get_sum_lower_points(c_map):
	width = len(c_map[0])
	height = len(c_map)
	summ = 0

	c_summ = 0
	def map_recursive(x, y):
		nonlocal c_map
		nonlocal c_summ

		c_height = c_map[y][x]
		if c_height != -1 and c_height!=9:
			c_map[y][x] = -1
			c_summ += 1

			if y>0:
				map_recursive(x, y-1)
			if y<height-1:
				map_recursive(x, y+1)
			if x>0:
				map_recursive(x-1, y)
			if x<width-1:
				map_recursive(x+1, y)

	basins = []
	for x in range(width):
		for y in range(height):
			c_height = c_map[y][x]
			if c_height != -1 and c_height != 9:
				c_summ = 0
				map_recursive(x, y)
				basins.append(c_summ)
	basins.sort()

	sol = 1
	for val in basins[::-1][:3]:
		sol *= val
	return sol 


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

	sol = get_sum_lower_points(height_map)
	print(sol)