
if __name__ == '__main__':
	with open('input.txt') as file:
		message = file.read().splitlines()[0]
		message = message.split('x=')[1]
		message = message.split(', y=')

		min_x, max_x = message[0].split('..')
		min_x = int(min_x)
		max_x = int(max_x)
		min_y, max_y = message[1].split('..')
		min_y = int(min_y)
		max_y = int(max_y)

	print(min_x, max_x)
	print(min_y, max_y)
