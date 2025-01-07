class Bingo:
	def __init__(self, c_numbers):
		self.board = []
		for j in range(5):
			self.board.append([])
			for i in range(5):
				val = c_numbers[j*5+i]
				self.board[j].append(val)

	def check_row(self, c_row):
		for i in range(5):
			if self.board[c_row][i] != -1:
				return False
		return True

	def check_column(self, c_column):
		for j in range(5):
			if self.board[j][c_column] != -1:
				return False
		return True

	def check_number(self, c_number):
		for j in range(5):
			for i in range(5):
				val = self.board[i][j]
				if val == c_number:
					self.board[i][j] = -1
					if(self.check_row(i)):
						return True
					if(self.check_column(j)):
						return True
					return False
		return False

	def get_sum(self):
		value = 0
		for j in range(5):
			for i in range(5):
				c_val = self.board[i][j]
				if c_val != -1:
					value += c_val
		return value

if __name__ == '__main__':
	with open('input.txt') as file:
		lines = file.read().splitlines()

		numbers = [int(n) for n in lines[0].split(',')]
		lines = lines[1:]

		boards = []
		while(len(lines)>=6):
			c_board = []

			foo = lines[1:6]
			for l in foo:
				[c_board.append(int(n)) for n in l.split()]
			boards.append(Bingo(c_board))

			lines = lines[6:]

	for n in numbers:
		next_try = []
		for b in boards:
			if b.check_number(n):
				if len(boards)==1:
					sol = b.get_sum()*n
					print(sol)
					exit()
			else:
				next_try.append(b)
		boards = next_try

