def syntax_scoring(c_line):
	chunks = {
		'(':')',
		'[':']',
		'{':'}',
		'<':'>',
	}
	heap = []
	for char in list(c_line):
		if char in chunks:
			heap.append(chunks[char])
		elif char in chunks.values():
			last = heap.pop()
			if last!=char:
				return char
	return False


if __name__ == '__main__':
	with open('input.txt') as file:
		lines = file.read().splitlines()

	sol = 0
	for line in lines:
		error = syntax_scoring(line)
		if error:
			if error==')':
				sol+=3
			elif error==']':
				sol+=57
			elif error=='}':
				sol+=1197
			elif error=='>':
				sol+=25137
	print(sol)