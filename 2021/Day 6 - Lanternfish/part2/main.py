if __name__ == '__main__':
	with open('input.txt') as file:
		states = [int(s) for s in file.readline().strip().split(',')]
		
		lanterfishes = {}
		for s in range(9):
			lanterfishes[s] = 0

		for s in states:
			lanterfishes[s] += 1

	for day in range(256):
		n_lantern = {}
		for s in reversed(range(1,9)):
			n_lantern[s-1] = lanterfishes[s]
		if 6 not in n_lantern:
			n_lantern[6] = 0
		n_lantern[6] += lanterfishes[0]
		n_lantern[8] = lanterfishes[0]
		lanterfishes = n_lantern

	sol = 0
	for key in lanterfishes:
		sol += lanterfishes[key]
	print(sol)

