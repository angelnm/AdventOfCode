def read_oxygen(c_diagnostic):
	c_scores = [0] * len(c_diagnostic[0])

	for idx in range(len(c_diagnostic[0])):
		c_ones = []
		c_zero = []
		for number in c_diagnostic:
			status = number[idx]
			if status == '1':
				c_ones.append(number)
			else:
				c_zero.append(number)
		if len(c_ones)>=len(c_zero):
			c_diagnostic = c_ones
		else:
			c_diagnostic = c_zero

		if len(c_diagnostic) == 1:
			return c_diagnostic[0]

def read_co2(c_diagnostic):
	c_scores = [0] * len(c_diagnostic[0])

	for idx in range(len(c_diagnostic[0])):
		c_ones = []
		c_zero = []
		for number in c_diagnostic:
			status = number[idx]
			if status == '1':
				c_ones.append(number)
			else:
				c_zero.append(number)
		if len(c_zero)<=len(c_ones):
			c_diagnostic = c_zero
		else:
			c_diagnostic = c_ones

		if len(c_diagnostic) == 1:
			return c_diagnostic[0]

def bin2dec(c_number):
	number = 0

	c_number = c_number[::-1]
	for idx, val in enumerate(c_number):
		if val == '1':
			number += pow(2, idx) 

	return number

if __name__ == '__main__':
	with open('input.txt') as file:
		diagnostic = file.readlines()
		diagnostic = [l.strip() for l in diagnostic]

	oxygen = bin2dec(read_oxygen(diagnostic))
	co2 = bin2dec(read_co2(diagnostic))
	life_support = oxygen*co2
	print(life_support)


