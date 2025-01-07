def myFunc(e):
	return e.distance

class Cell:
	def __init__(self, _x, _y, _risk):
		self.visited = False
		self.distance = -1
		self.father = None

		self.x = _x
		self.y = _y
		self.risk = _risk

if __name__ == '__main__':
	with open('input.txt') as file:
		scan = file.read().splitlines()

		map_risk =  []
		for y, line in enumerate(scan):
			foo = []
			for x, risk in enumerate(line):
				foo.append(Cell(x, y, int(risk)))
			map_risk.append(foo)

	height = len(map_risk)
	width  = len(map_risk[0])

	start_point = map_risk[0][0]
	start_point.distance = 0
	start_point.visited = True
	queue = [start_point]
	def check_add(point1, point2):
		new_distance = point1.distance + point2.risk
		if not point2.visited:
			point2.distance = new_distance
			point2.visited = True
			queue.append(point2)
		else:
			if new_distance < point2.distance:
				point2.distance = new_distance
				if point2 not in queue:
					queue.append(point2)

	while len(queue)>0:
		queue.sort(reverse=True, key=myFunc)
		c_point = queue.pop()
		c_x = c_point.x
		c_y = c_point.y

		if c_x>0: #Puede ir a la izquierda
			check_add(c_point, map_risk[c_y][c_x-1])
		if c_x<width-1: # Puede ir a la derecha
			check_add(c_point, map_risk[c_y][c_x+1])
		if c_y>0: #Puede ir hacia abajo
			check_add(c_point, map_risk[c_y-1][c_x])
		if c_y<height-1: # Puede ir hacia arriba
			check_add(c_point, map_risk[c_y+1][c_x])

	"""
	for y in range(height):
		string = ''
		for x in range(width):
			string +=str(map_risk[y][x].distance) +' '
		print(string)
	"""

	print(map_risk[height-1][width-1].distance)






