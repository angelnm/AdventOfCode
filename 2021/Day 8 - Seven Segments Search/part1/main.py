if __name__ == '__main__':
	with open('input.txt') as file:
		lines = file.read().splitlines()
		lines = [line.split('|') for line in lines]
		lines = [[line[0].split(), line[1].split()] for line in lines]

	n_count = 0
	for entry in lines:
		digits = entry[1]
		for digit in digits:
			length = len(digit)
			if length==2 or length==4 or length==3 or length==7:
				n_count += 1
	print(n_count) 