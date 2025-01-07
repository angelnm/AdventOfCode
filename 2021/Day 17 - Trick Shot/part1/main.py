
if __name__ == '__main__':
	with open('input.txt') as file:
		message = file.read().splitlines()[0]
		message = message.split('y=')[1]
		message = message.split('..')[0]
		message = abs(int(message))

	n = 0
	for i in range(message):
		n+=i
	print(n)