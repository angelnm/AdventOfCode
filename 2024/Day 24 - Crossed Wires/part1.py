
def read_file(nameFile):
	file = open(nameFile, 'r')
	variables, orders = file.read().split('\n\n')

	memory = {}
	for line in variables.split('\n'):
		name, value = line.split(':')
		if name not in memory:
			memory[name] = 0
		memory[name] = int(value)

	wires = []
	for line in orders.split('\n'):
		function, var = line.split(' -> ')
		n1, op, n2 = function.split(' ')

		wires.append([n1, op, n2, var])

	pos = 0
	while wires:
		pos = pos%len(wires)
		c_wire = wires[pos]

		n1 = c_wire[0]
		n2 = c_wire[2]

		if n1 not in memory or n2 not in memory:
			pos += 1
			continue

		op = c_wire[1]
		var = c_wire[3]
		if op == 'AND':
			result = memory[n1] and memory[n2]
		elif op == 'OR':
			result = memory[n1] or memory[n2]
		elif op == 'XOR':
			result = memory[n1] ^ memory[n2]

		memory[var] = result
		wires.pop(pos)

	return memory


def main():
	memory = read_file('input2.txt')
	number = 0
	for key in memory:
		if key[0] == 'z':
			power = int(key[1:])
			number += pow(2, power)*memory[key]
	print(number)

main()