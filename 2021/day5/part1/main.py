def check_overlap(c_lines):
	overlaps = {}
	n_overlaps = 0
	def add_point(c_x, c_y):
		nonlocal overlaps
		nonlocal n_overlaps
		if c_x not in overlaps:
			overlaps[c_x] = {}
		if c_y not in overlaps[c_x]:
			overlaps[c_x][c_y] = 0
		overlaps[c_x][c_y] += 1
		if overlaps[c_x][c_y] == 2:
			n_overlaps += 1

	for line in c_lines:
		x1, y1 = [int(n) for n in line[0].split(',')]
		x2, y2 = [int(n) for n in line[1].split(',')]

		if x1==x2:
			if y1 > y2:
				tmp = y1
				y1 = y2
				y2 = tmp
			for c_y in range(y1, y2+1):
				add_point(x1, c_y)
		elif y1==y2:
			if x1 > x2:
				tmp = x1
				x1 = x2
				x2 = tmp
			for c_x in range(x1, x2+1):
				add_point(c_x, y1)

	return n_overlaps


if __name__ == '__main__':
	with open('input.txt') as file:
		lines = [ l.split('->') for l in file.read().splitlines()]

	sol = check_overlap(lines)
	print(sol)