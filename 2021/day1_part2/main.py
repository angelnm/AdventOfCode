def sliding_window(c_size, c_list):
	n_list = []

	for idx, depth in enumerate(c_list[:-(c_size-1)]):
		window = 0
		for i in range(c_size):
			window += c_list[idx+i]
		n_list.append(window)

	return n_list

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

	values = sliding_window(3, values)
	sol = count_increment(values)
	print(sol)




