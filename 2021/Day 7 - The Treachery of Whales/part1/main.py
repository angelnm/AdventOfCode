if __name__ == '__main__':
	with open('input.txt') as file:
		positions = [int(s) for s in file.readline().strip().split(',')]
		positions.sort()

	median = positions[int(len(positions)/2)]
	fuel = 0
	for p in positions:
		fuel += abs(p-median)
	print(fuel)
