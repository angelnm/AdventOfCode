def follow_commands(c_commands):
	depth = 0
	horzt = 0
	aim = 0

	def go_forward(val):
		nonlocal horzt
		nonlocal depth
		horzt += val
		depth += aim*val
	def go_down(val):
		nonlocal aim
		aim += val
	def go_up(val):
		nonlocal aim
		aim -= val

	functions = {
		'forward': go_forward,
		'down': go_down,
		'up': go_up,
	}

	for command in c_commands:
		order = command[0]
		value = int(command[1])
		functions[order](value)

	return depth*horzt


if __name__ == '__main__':
	with open('input.txt') as file:
		commands = file.readlines()
		commands = [l.split() for l in commands]


	sol = follow_commands(commands)
	print(sol)


