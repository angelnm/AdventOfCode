if __name__ == '__main__':
	with open('input.txt') as file:
		cont = True
		l_points = []
		while(cont):
			line = file.readline().strip()
			if line=='':
				cont = False
			else:
				l_points.append(line)

		folds = file.read().splitlines()
		folds = folds[:1]

	c_points = {}
	for point in l_points:
		x,y = point.split(',')
		x = int(x)
		y = int(y)
		if x not in c_points:
			c_points[x] = []
		c_points[x].append(y)

	for fold in folds:
		_,_,data = fold.split()
		axis,number = data.split('=')
		number = int(number)

		n_points = {}
		for c_x in c_points:
			for c_y in c_points[c_x]:
				if axis == 'x':
					if c_x == number:
						continue
					elif c_x < number:
						x = c_x
					else:
						x = number - (c_x-number)
					y = c_y
				elif axis == 'y':
					x = c_x
					if c_y == number:
						continue
					elif c_y < number:
						y = c_y
					else:
						y = number - (c_y-number)
				if x not in n_points:
					n_points[x] = []
				if y not in n_points[x]:
					n_points[x].append(y)
		c_points = n_points

	sol = 0
	for c_x in c_points:
		sol+=len(c_points[c_x])
	print(sol)