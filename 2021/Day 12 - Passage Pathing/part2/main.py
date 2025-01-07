class Node:
	def __init__(self, c_name):
		self.name = c_name
		self.conn = []

	def addConnection(self, c_node):
		self.conn.append(c_node)

	def connectedCaves(self, c_history):
		counter = []
		cheat = False
		for hist in c_history:
			name = hist.name
			if name.islower() and name!='start':
				if hist in counter:
					cheat = True
					break
				else:
					counter.append(hist)

		n_list = []
		for conn in self.conn:
			if conn.name.isupper() or conn not in c_history:
				n_list.append(conn)
			elif conn.name.islower() and conn.name != 'start' and not cheat:
				n_list.append(conn)
		return n_list

def process_map(c_lines):
	caves = {}

	for connection in c_lines:
		caveA, caveB = connection.split('-')
		if caveA not in caves:
			caves[caveA] = Node(caveA)
		if caveB not in caves:
			caves[caveB] = Node(caveB)
		caveA = caves[caveA]
		caveB = caves[caveB]

		caveA.addConnection(caveB)
		caveB.addConnection(caveA)

	return caves

def possible_routes(c_map):
	c_node = [c_map['start']]
	paths = 0

	def explore(c_hist):
		nonlocal paths

		connections = c_hist[-1].connectedCaves(c_hist)
		for child in connections:
			copy_hist = c_hist.copy()
			copy_hist.append(child)
			if child.name != 'end':
				explore(copy_hist)
			else:
				#print(','.join([h.name for h in copy_hist]))
				paths += 1
	explore(c_node)
	return paths

if __name__ == '__main__':
	with open('input.txt') as file:
		lines = file.read().splitlines()

	c_map = process_map(lines)
	sol = possible_routes(c_map)
	print(sol)
