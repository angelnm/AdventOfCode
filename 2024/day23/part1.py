

def read_file(nameFile):
	file = open(nameFile, 'r')

	nodes = {}
	for line in file:
		line = line.rstrip()

		first, second = line.split('-')
		if first not in nodes:
			nodes[first] = []
		if second not in nodes:
			nodes[second] = []
		nodes[first].append(second)
		nodes[second].append(first)

	return nodes

def search_multiplayer(nodes):
	total = 0
	while nodes:
		node = next(iter(nodes))
		connections = nodes[node]
		nodes.pop(node)

		for idx, con in enumerate(connections):
			for con2 in connections[idx+1:]:
				if con not in nodes or con2 not in nodes:
					continue
				if con2 in nodes[con]:
					if 't' in (node[0]+con[0]+con2[0]):
						print(node, con, con2)
						total += 1

	print(total)

def main():
	nodes = read_file('input2.txt')
	search_multiplayer(nodes)

main()