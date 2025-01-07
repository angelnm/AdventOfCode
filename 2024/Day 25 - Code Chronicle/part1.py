FILE = 'input2.txt'

def read_file(fileName):
	file = open(fileName, 'r')
	elements = file.read().split('\n\n')

	locks = []
	keys = []

	for el in elements:
		lines = el.split('\n')
		if lines[0] == '#'*5:
			locks.append(lines)
		else:
			keys.append(lines)

	data_lock = []
	for lock in locks:
		c_lock = [-1]*5
		for y, line in enumerate(lock):
			for x, data in enumerate(line):
				if c_lock[x] == -1 and data == '.':
					c_lock[x] = y-1
		data_lock.append(c_lock)

	data_key = []
	for key in keys:
		c_key = [-1]*5
		for y, line in enumerate(key):
			for x, data in enumerate(line):
				if c_key[x] == -1 and data == '#':
					c_key[x] = 6-y
		data_key.append(c_key)

	return data_lock, data_key

def compare_lk(locks, keys):
	fit = 0

	for key in keys:
		for lock in locks:
			itFit = True
			for k, l in zip(key, lock):
				if k+l>5:
					itFit = False
					break
			if itFit:
				fit += 1
	print(fit)

def main():
	locks, keys = read_file(FILE)
	compare_lk(locks, keys)

main()