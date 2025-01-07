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

def compute_secret(secret_number, times):
	#print(f"Computing Secret Number {secret_number}")
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

		#print(f"{ite+1}: {secret_number}")
	return secret_number

def main():
	numbers = read_secret_number('input1.txt')

	total = 0
	for number in numbers:
		secret = compute_secret(number,2000)
		total += secret
	print(total)

main()