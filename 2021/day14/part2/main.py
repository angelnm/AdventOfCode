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

	dic_polymer = {}
	for i in range(len(polymer)-1):
		c_element = polymer[i]
		n_element = polymer[i+1]
		pair = c_element+n_element

		if pair not in dic_polymer:
			dic_polymer[pair] = 0
		dic_polymer[pair] += 1

	for i in range(40):
		n_dic_polymer = {}
		for pair in dic_polymer:
			left_element = pair[0]
			rigt_element = pair[1]
			midl_element = rules[pair]

			n1_pair = left_element+midl_element
			n2_pair = midl_element+rigt_element

			if n1_pair not in n_dic_polymer:
				n_dic_polymer[n1_pair]=0
			n_dic_polymer[n1_pair]+=dic_polymer[pair]

			if n2_pair not in n_dic_polymer:
				n_dic_polymer[n2_pair]=0
			n_dic_polymer[n2_pair]+=dic_polymer[pair]

		dic_polymer = n_dic_polymer

	counter = {}
	for pair in dic_polymer:
		left_element = pair[0]
		rigt_element = pair[1]

		if left_element not in counter:
			counter[left_element]=0
		if rigt_element not in counter:
			counter[rigt_element]=0

		counter[left_element] += dic_polymer[pair]
		counter[rigt_element] += dic_polymer[pair]
	counter[polymer[0]]+=1
	counter[polymer[-1]]+=1

	most_common = -1
	least_common = -1
	for element in counter:
		value = int(counter[element]/2)
		if most_common==-1 or value>most_common:
			most_common = value
		if least_common==-1 or value<least_common:
			least_common = value
	print(most_common-least_common)
