if __name__ == '__main__':
	with open('input.txt') as file:
		# file.readline().strip()

		polymer = file.readline().rstrip('\n')
		file.readline()
		R_rules = file.read().splitlines()


	# Read rules
	rules = {}
	for rule in R_rules:
		pair, _, result = rule.split()
		rules[pair] = result

	for n in range(10):
		n_polymer = ''
		for i in range(len(polymer)-1):
			c_element = polymer[i]
			n_element = polymer[i+1]
			pair = c_element+n_element

			n_polymer += c_element
			if(pair)in rules:
				n_polymer+=rules[pair]
		n_polymer += polymer[-1]
		polymer = n_polymer

	counter = {}
	for element in polymer:
		if element not in counter:
			counter[element]=0
		counter[element] += 1

	most_common = -1
	least_common = -1
	for element in counter:
		value = counter[element]
		if most_common==-1 or value>most_common:
			most_common = value
		if least_common==-1 or value<least_common:
			least_common = value
	print(most_common-least_common)
