from random import randint

# gbj,mkt,mps,vcv,vwp,z13,z19,z25

class Gen:
	def __init__(self, gen_max, gen_len):
		self.data = [-1]*gen_len
		self.gen_max = gen_max

		self.result = -1
		self.total_score = 0
		self.score = 0

		self.tries = 0
		self.times = 0

	def new_datavalue(self):
		r = randint(0, self.gen_max)
		while r in self.data:
			r = randint(0, self.gen_max)
		return r

	def reorder(self):
		data = []
		for i in range(0, len(self.data), 2):
			a = self.data[i]
			b = self.data[i+1]
			if a<b:
				data.append([a, b])	
			else:
				data.append([b,a])
		data = sorted(data, key= lambda x: x[0])

		self.data = []
		for d in data:
			self.data.append(d[0])
			self.data.append(d[1])


	def init_data(self):
		for i in range(len(self.data)):
			r = self.new_datavalue()
			self.data[i] = r
		self.reorder()

	def mutate(self):
		n_gen = Gen(self.gen_max, len(self.data))

		for i in range(len(self.data)):
			prob = randint(0,99)
			if prob < 50 or self.data[i] in n_gen.data:
				r = n_gen.new_datavalue()
				n_gen.data[i] = r
			else:
				n_gen.data[i] = self.data[i]

		prob = randint(0,99)
		if prob < 40:
			pos1 = randint(0, len(self.data)-1)
			pos2 = randint(0, len(self.data)-1)
			tmp = n_gen.data[pos1]
			n_gen.data[pos1] = n_gen.data[pos2]
			n_gen.data[pos2] = tmp

		n_gen.reorder()

		return n_gen

	def set_result(self, result):
		self.result = result

	def set_score(self, result, wanted):
		r = bin(result)[2:]
		w = bin(wanted)[2:]
		
		score = 0
		for idx in range(len(w)):
			if len(r) <= idx:
				break
			if r[-1-idx] == w[-1-idx]: 
				score += 1

		self.total_score += score/len(w)
		self.tries += 1

		if r == w:
			self.times += 1
		else:
			self.times -= 0.05
			self.times = max(1, self.times)

		self.score = self.total_score/self.tries
		#self.score += randint(0,1000)
		#self.score *= self.times

	def __lt__(self, obj):
		return ((self.score) < (obj.score))

	def __gt__(self, obj):
		return ((self.score) > (obj.score))

	def __le__(self, obj):
		return ((self.score) <= (obj.score))

	def __ge__(self, obj):
		return ((self.score) >= (obj.score))

	def __eq__(self, obj):
		return (self.score == obj.score)

	def __repr__(self):
		return f"{self.times:.2f} {self.score:.2f} {self.tries} {self.data} {bin(self.result)[2:]} "

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

	return memory, wires

def compute_wires(memory, wires):
	pos = 0
	last = pos
	while wires:
		pos = pos%len(wires)
		c_wire = wires[pos]

		n1 = c_wire[0]
		n2 = c_wire[2]

		if n1 not in memory or n2 not in memory:
			pos += 1
			if pos%len(wires) == last:
				break
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
		last = pos%len(wires) if len(wires)>0 else 0

	return memory

def read_number(memory, letter):
	number = 0
	for key in memory:
		if key[0] == letter:
			power = int(key[1:])
			number += pow(2, power) * memory[key]
	return number

def try_gen(memory_c, wires_c, gen):
	wires = []
	for w in wires_c:
		wires.append(w.copy())

	memory = memory_c.copy()
	for key in memory:
		r = randint(0,1)
		memory[key] = r

	xs = read_number(memory, 'x')
	ys = read_number(memory, 'y') 
	ws = xs + ys

	for idx in range(0, len(gen.data), 2):
		a = gen.data[idx+0]
		b = gen.data[idx+1]

		tmp = wires[a][3]
		wires[a][3] = wires[b][3]
		wires[b][3] = tmp

	compute_wires(memory, wires)
	result = read_number(memory, 'z')

	gen.set_result(result)
	gen.set_score(result, ws)

def genetic_swaps(memory, wires, n_swaps, gen_size=100):
	# Generate First Gens
	gens = []
	for _ in range(gen_size):
		n_gen = Gen(len(wires)-1, n_swaps*2)
		n_gen.init_data()
		gens.append( n_gen )
	gens[0].data = [4, 51, 7, 46, 83, 159, 111, 141]

	while gens[0].times <= 500:
		# Score them and mutate
		for g in gens:
			try_gen(memory, wires, g)

		# Sort them by score
		keep = max(1, int(gen_size*0.05))
		n_gens = []

		tmp_g = sorted(gens, key=lambda x: x.times, reverse=True)
		n_gens.extend(tmp_g[:keep])
		for g in n_gens:
			print(g)

		tmp_g = sorted(gens, key=lambda x: x.score, reverse=True)
		for g in tmp_g[:keep]:
			if g not in n_gens:
				n_gens.append(g)

		for g in gens:
			if g.score >= 0.95 and g not in n_gens:
				n_gens.append(g)

		# Keep 10% and generate news until fill
		pos = 0
		while pos < len(n_gens):
			for g in reversed(n_gens[pos+1:]):
				if n_gens[pos].data == g.data:
					n_gens.remove(g)
			pos += 1

		#for g in n_gens[:50]:
		#	print(g)
		#print()
		print(keep, len(n_gens))
		while len(n_gens) < int(gen_size*0.8):
			father = randint(0, keep-1)
			n_g = n_gens[father].mutate()
			n_gens.append(n_g)

		while len(n_gens) < gen_size:
			n_g = Gen(len(wires)-1, n_swaps*2)
			n_g.init_data()
			n_gens.append( n_g )
		#n_gens[-1].data = [7,77,51,4,141,111,159,83]

		gens = n_gens

	perfect = gens[0]
	result = []
	for i in perfect.data:
		result.append(wires[i][3])
	result.sort()
	print(','.join(result))


def main():
	memory, wires = read_file('input2.txt')
	genetic_swaps(memory, wires, 4)


main()