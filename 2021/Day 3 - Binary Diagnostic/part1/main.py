def read_diagnostic(c_diagnostic):
	c_scores = [0] * len(c_diagnostic[0])

	for number in c_diagnostic:
		for idx, status in enumerate(number):
			foo = 1
			if status == '0':
				foo = -1
			c_scores[idx] += foo

	gamma = ''
	epsilon = ''
	for score in c_scores:
		if score >= 0:
			gamma = gamma+'1'
			epsilon = epsilon+'0'
		else:
			gamma = gamma+'0'
			epsilon = epsilon+'1'

	return gamma, epsilon

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

	gamma, epsilon = read_diagnostic(diagnostic)
	gamma = bin2dec(gamma)
	epsilon = bin2dec(epsilon)

	power_consumption = gamma*epsilon
	print(power_consumption)


