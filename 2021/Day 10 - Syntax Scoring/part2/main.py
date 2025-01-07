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
				return False
	return heap[::-1]


if __name__ == '__main__':
	with open('input.txt') as file:
		lines = file.read().splitlines()

	l_scores = []
	for line in lines:
		complete = syntax_scoring(line)
		if complete:
			score = 0
			for char in complete: 
				score *= 5
				if char==')':
					score+=1
				elif char==']':
					score+=2
				elif char=='}':
					score+=3
				elif char=='>':
					score+=4
			l_scores.append(score)
	l_scores.sort()
	
	sol = l_scores[int(len(l_scores)/2)]
	print(sol)

