class Octopus:
	flash = 0

	def __init__(self, c_energy):
		self.energy = c_energy
		self.n_update = -1
		self.neighbors = []

	def setNeighbors(self, n_list):
		self.neighbors = n_list

	def nextStep(self, step):
		if self.n_update!=step:
			self.energy += 1
			if self.energy > 9:
				Octopus.flash += 1
				self.n_update=step
				self.energy=0
				for neighbor in self.neighbors:
					neighbor.nextStep(step)


if __name__ == '__main__':
	with open('input.txt') as file:
		lines = file.read().splitlines()
		for idx, line in enumerate(lines):
			line = list(line)
			line = [int(l) for l in line]
			lines[idx] = line

	l_octopus = []
	for y in range(len(lines)):
		l_octopus.append([])
		for x in lines[y]:
			l_octopus[y].append(Octopus(x))

	for y in range(len(l_octopus)):
		for x in range(len(l_octopus[0])):
			
			neighbors = []
			for c_y in range(max(0,y-1),min(len(l_octopus),y+2)):
				for c_x in range(max(0,x-1),min(len(l_octopus[0]),x+2)):
					if c_y!=y or c_x!=x:
						neighbors.append(l_octopus[c_y][c_x])
			l_octopus[y][x].setNeighbors(neighbors)

	def draw_status():
		for y in range(len(l_octopus)):
			string = ''
			for x in range(len(l_octopus[0])):
				string += str(l_octopus[y][x].energy)
			print(string)

	diff = 0
	step = 0
	while diff!=100:
		#print('After step {}:'.format(step))
		#draw_status()
		#print()

		current = Octopus.flash
		for y in range(len(l_octopus)):
			for x in range(len(l_octopus[0])):
				l_octopus[y][x].nextStep(step)
		diff = Octopus.flash - current
		step += 1

	#print('After step {}:'.format(step+1))
	#draw_status()
	print(step)

