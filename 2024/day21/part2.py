"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
v<<A>>^A<A>AvA<^AA>A<vAAA>^A
<A^A>^^AvvvA
029A
"""
import math

D_NUMPAD = {
	'7': [0,0],
	'8': [1,0],
	'9': [2,0],
	'4': [0,1],
	'5': [1,1],
	'6': [2,1],
	'1': [0,2],
	'2': [1,2],
	'3': [2,2],
	'0': [1,3],
	'A': [2,3]
}

D_DIRPAD = {
	'^': [1,0],
	'A': [2,0],
	'<': [0,1],
	'v': [1,1],
	'>': [2,1]
}

NUMPAD = 0
DIRPAD = 1

def get_dir_y(dist_y):
	seq = ""
	if dist_y < 0:
		seq += '^' * abs(dist_y)
	if dist_y > 0:
		seq += 'v' * dist_y
	return seq

def get_dir_x(dist_x):
	seq = ""
	if dist_x < 0:
		seq += '<' * abs(dist_x)
	if dist_x > 0:
		seq += '>' * dist_x
	return seq

def get_numpad_move(key_start, key_to):
	sequences = []

	pos_str = D_NUMPAD[key_start]
	pos_end = D_NUMPAD[key_to]

	dist_x = pos_end[0] - pos_str[0]
	dist_y = pos_end[1] - pos_str[1]

	#print(pos_str, pos_end, dist_x, dist_y)
	if dist_x != 0 and not (pos_str[1]==3 and pos_str[0]+dist_x == 0):
		seq = ""
		seq += get_dir_x(dist_x)
		seq += get_dir_y(dist_y)
		seq += 'A'
		sequences.append(seq)
	if dist_y != 0 and not (pos_str[0]==0 and pos_str[1]+dist_y == 3):
		seq = ""
		seq += get_dir_y(dist_y)
		seq += get_dir_x(dist_x)
		seq += 'A'
		sequences.append(seq)
	#print(sequences)
	return sequences

def get_dirpad_move(key_start, key_to):
	sequences = []

	pos_str = D_DIRPAD[key_start]
	pos_end = D_DIRPAD[key_to]

	dist_x = pos_end[0] - pos_str[0]
	dist_y = pos_end[1] - pos_str[1]

	if dist_x != 0 and not (pos_str[1]==0 and pos_str[0]+dist_x == 0):
		seq = ""
		seq += get_dir_x(dist_x)
		seq += get_dir_y(dist_y)
		seq += 'A'
		sequences.append(seq)
	if dist_y != 0 and not (pos_str[0]==0 and pos_str[1]+dist_y == 0):
		seq = ""
		seq += get_dir_y(dist_y)
		seq += get_dir_x(dist_x)
		seq += 'A'
		sequences.append(seq)
	if dist_x == 0 and dist_y == 0:
		sequences.append('A')

	return sequences

def process_code(code, rec=0):
	if rec<=0:
		return code

	type = NUMPAD if code[0]>='0' and code[0]<='9' else DIRPAD
	new_code = ""
	for last_key, key in zip('A'+code[:-1], code):
		if type == NUMPAD:
			codes = get_numpad_move(last_key, key)
		elif type == DIRPAD:
			codes = get_dirpad_move(last_key, key)

		sc = ""
		min_length = math.inf
		for c in codes:
			sub_code = process_code(c, rec-1)
			if len(sub_code)<min_length:
				min_length = len(sub_code)
				sc = sub_code
		new_code += sc

	return new_code

def process_codes_ite(codes, ite):
	for i in range(ite):
		new_codes = {}
		for code in codes:
			times = codes[code]
			type = NUMPAD if code[0]>='0' and code[0]<='9' else DIRPAD

			for last_key, key in zip('A'+code[:-1], code):
				if type == NUMPAD:
					sub_c = get_numpad_move(last_key, key)
				elif type == DIRPAD:
					sub_c = get_dirpad_move(last_key, key)
				

				sc = ""
				min_length = math.inf
				for c in sub_c:
					sub_code = process_code(c, 4)
					if len(sub_code) < min_length:
						min_length = len(sub_code)
						sc = c

				if sc not in new_codes:
					new_codes[sc] = 0
				new_codes[sc] += times
		#print(new_codes)
		codes = new_codes

	total = 0
	for key in codes:
		total += len(key) * codes[key] 
	return total


def get_number(code):
	return int(code[:-1])

def main():
	file = open('input1.txt', 'r')

	total  = 0
	for line in file:
		line = line.rstrip()

		codes = {line:1}
		interactions = process_codes_ite(codes, 26)
		#interactions = process_code(line, 3)
		number = get_number(line)

		#print(interactions)
		print(interactions, number)

		total += number * interactions
	print(total)
		

main()