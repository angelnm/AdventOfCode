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

		xdiff = x2 - x1
		ydiff = y2 - y1

		if xdiff==0 or ydiff==0 or abs(xdiff)==abs(ydiff):
			steps = max(abs(xdiff), abs(ydiff))
			for step in range(steps+1):
				c_x = x1
				if xdiff!=0:
					sign = int(abs(xdiff)/xdiff)
					c_x += step*sign
				c_y = y1
				if ydiff!=0:
					sign = int(abs(ydiff)/ydiff)
					c_y += step*sign
				add_point(c_x, c_y)

	return n_overlaps


if __name__ == '__main__':
	with open('input.txt') as file:
		lines = [ l.split('->') for l in file.read().splitlines()]

	sol = check_overlap(lines)
	print(sol)