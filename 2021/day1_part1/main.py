def count_increment(c_list):
	n_increased = 0
	pre_depth = c_list[0]

	for depth in c_list[1:]:
		if(depth > pre_depth):
			n_increased +=1
		pre_depth = depth

	return n_increased


if __name__ == '__main__':
	with open('input.txt') as file:
		values = [int(line) for line in file]

	sol = count_increment(values)
	print(sol)




