class Lanterfish:
	def __init__(self, c_counter):
		self.counter = c_counter

	def new_day(self):
		self.counter -= 1
		if self.counter == -1:
			self.counter = 6
			return True
		return False

if __name__ == '__main__':
	with open('input.txt') as file:
		states = [int(s) for s in file.readline().strip().split(',')]
		lanterfishes = [Lanterfish(s) for s in states]

	for day in range(80):
		nl_lantern = []
		for fish in lanterfishes:
			nl_lantern.append(fish)
			if fish.new_day():
				nl_lantern.append(Lanterfish(8))
		lanterfishes = nl_lantern
	sol = len(lanterfishes)
	print(sol)

