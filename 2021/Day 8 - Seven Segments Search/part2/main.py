def decode_entry(c_entry):
	codes, digits = entry

	decode = {}
	for i in range(10):
		decode[i] = set()
	def update_decode(c_true, c_lines):
		nonlocal decode
		for number in c_true:
			decode[number].update(c_lines)

	decode_data = {
		2:[],
		3:[],
		4:[],
		5:[],
		6:[],
		7:[],
	}
	for code in codes:
		code = ''.join(sorted(code))
		decode_data[len(code)].append(code)

	# 1
	code = decode_data[2][0]
	del decode_data[2]
	update_decode([1], set(code))
	# 4
	code = decode_data[4][0]
	del decode_data[4]
	update_decode([4], set(code))
	# 7
	code = decode_data[3][0]
	del decode_data[3]
	update_decode([7], set(code))
	# 8
	code = decode_data[7][0]
	del decode_data[7]
	update_decode([8], set(code))
	# 0
	code = decode[4]
	code = code.intersection(decode_data[5][0])
	code = code.intersection(decode_data[5][1])
	code = code.intersection(decode_data[5][2])
	code = decode[8].difference(code)
	update_decode([0], code)
	decode_data[6].remove(''.join(sorted(code)))
	# 2
	code = set(decode_data[6][0])
	code = code.intersection(decode_data[6][1])
	code = decode[8].difference(code)
	for n in decode_data[5]:
		s_n = set(n)
		if len(s_n.intersection(code)) == 2:
			update_decode([2], s_n)
			decode_data[5].remove(n)
			break
	# 3
	for n in decode_data[5]:
		s_n = set(n)
		if len(s_n.intersection(decode[2]))==4:
			update_decode([3], s_n)
			decode_data[5].remove(n)
			break
	# 5
	code = decode_data[5][0]
	del decode_data[5]
	update_decode([5], set(code))
	# 9
	for n in decode_data[6]:
		s_n = set(n)
		if len(s_n.intersection(decode[4]))==4:
			update_decode([9], s_n)
			decode_data[6].remove(n)
			break
	# 6
	code = decode_data[6][0]
	del decode_data[6]
	update_decode([6], set(code))


	decoder = {}
	for d in decode:
		decoder[''.join(sorted(decode[d]))] = d

	number = 0
	for idx, digit in enumerate(digits):
		digit = ''.join(sorted(digit))
		digit = decoder[digit]
		number += digit*pow(10,3-idx)

	return number

if __name__ == '__main__':
	with open('input.txt') as file:
		lines = file.read().splitlines()
		lines = [line.split('|') for line in lines]
		lines = [[line[0].split(), line[1].split()] for line in lines]

	sol = 0
	for entry in lines:
		sol += decode_entry(entry)
	print(sol)