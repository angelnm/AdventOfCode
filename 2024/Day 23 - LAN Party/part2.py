

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

def check_max(nodes, current, connections):
	my_max = current
	for idx, con in enumerate(connections):
		if con not in nodes:
			continue

		connected = True
		to_check = nodes[con]
		for c in current:
			if c not in to_check:
				connected = False

		if not connected:
			continue

		#print(current + [con])
		tmp = check_max(nodes, current+[con], connections[idx+1:])
		if len(tmp) > len(my_max):
			my_max = tmp

	return my_max

def search_multiplayer(nodes):
	max_conn = []
	while nodes:
		node = next(iter(nodes))
		connections = nodes[node]
		nodes.pop(node)

		best = check_max(nodes, [node], connections)
		if len(best) > len(max_conn):
			max_conn = best

	max_conn.sort()
	print(','.join(max_conn))

def main():
	nodes = read_file('input2.txt')
	search_multiplayer(nodes)

main()