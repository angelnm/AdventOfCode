def read_secret_number(nameFile):
	file = open(nameFile, 'r')

	numbers = []
	for line in file:
		n = int(line)
		numbers.append(n)

	return numbers

def mixing(secret, number):
	return secret ^ number

def prune(secret):
	return secret%16777216

def compute_secret(secret_number, times, mega_code):
	#print(f"Computing Secret Number {secret_number}")
	first_n = [secret_number%10]
	for ite in range(times):
		number = secret_number * 64
		secret_number = mixing(secret_number, number)
		secret_number = prune(secret_number)

		number = secret_number //  32
		secret_number = mixing(secret_number, number)
		secret_number = prune(secret_number)

		number = secret_number * 2048
		secret_number = mixing(secret_number, number)
		secret_number = prune(secret_number)

		first_n.append(secret_number%10)

		#print(f"{ite+1}: {secret_number}")
	
	banana_code = {}
	pos = 4
	n_numbers = len(first_n)
	while pos < n_numbers:
		a = first_n[pos-3] - first_n[pos-4]
		b = first_n[pos-2] - first_n[pos-3]
		c = first_n[pos-1] - first_n[pos-2]
		d = first_n[pos-0] - first_n[pos-1]
		code = str(a) + str(b) + str(c) + str(d)

		bananas = first_n[pos]
		pos += 1

		if code not in banana_code:
			banana_code[code] = bananas

	for key in banana_code:
		if key not in mega_code:
			mega_code[key] = 0
		mega_code[key] += banana_code[key]


def main():
	numbers = read_secret_number('input2.txt')

	mega_code = {}
	for number in numbers:
		secret = compute_secret(number,2000, mega_code)

	b_max = 0
	for key in mega_code:
		if mega_code[key] > b_max:
			b_max = mega_code[key]
	print(b_max)

main()