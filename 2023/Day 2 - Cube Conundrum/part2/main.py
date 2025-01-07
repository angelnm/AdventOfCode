with open('input.txt', 'r') as fichero:
	 lines = fichero.read().splitlines()

total = 0
for line in lines:
	game_id, game_sets = line.split(': ')
	_, game_id = game_id.split( )

	game = [0,0,0]
	game_sets = game_sets.split('; ')
	for gSet in game_sets:
		gSet = gSet.split(', ')

		c_game = [0,0,0]
		for ball in gSet:
			n, color = ball.split(' ')
			if color == 'red':
				c_game[0] += int(n)
			elif color == 'green':
				c_game[1] += int(n)
			elif color == 'blue':
				c_game[2] += int(n)
		
		game[0] = max(game[0], c_game[0])
		game[1] = max(game[1], c_game[1])
		game[2] = max(game[2], c_game[2])


	total += game[0]*game[1]*game[2]
print(total)

