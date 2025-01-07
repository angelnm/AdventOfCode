import math

if __name__ == '__main__':
	with open('input.txt') as file:
		positions = [int(s) for s in file.readline().strip().split(',')]

	average = 0
	for p in positions:
		average += p
	average = int(average/len(positions))

	fuel1 = 0
	for p in positions:
		distance = abs(p-average)
		for d in range(distance):
			fuel1 += d+1

	fuel2 = 0
	for p in positions:
		distance = abs(p-average)
		for d in range(distance):
			fuel2 += d+1

	if fuel2<fuel1:
		fuel1 = fuel2
	print(fuel1)
