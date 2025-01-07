class mapPos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'(x={self.x} y={self.y})'

def read_map(nameFile):
    file = open(nameFile, 'r')
    
    cont = 0
    c_map = []
    start = None
    for line in file:
        line = line.rstrip('\n')
        c_map.append(line)
        cont += 1
        if 'S' not in line:
            continue
        new_str = ''
        for idx, letter in enumerate(line):
            if letter == 'S':
                start = mapPos(idx, cont-1)
                new_str += '.'
                continue
            new_str += letter
            c_map[-1] = new_str
                    
    return c_map, start

def check_pos(c_map, x, y, char='.'):
    x = x % len(c_map[0])
    y = y % len(c_map)
    
    if c_map[y][x] == char:
        return True
    return False
 
def add_pos(l_pos, pos, d_map):
    x = pos.x
    y = pos.y
    
    if x not in d_map:
        d_map[x] = {}
    if y not in d_map[x]:
        d_map[x][y] = False
    
    if d_map[x][y] == False:
        d_map[x][y] = True
        l_pos.append(pos)

def move(c_map, last_pos, previous):
    n_pos = []
    
    l_move  = [[-1,0],[+1,0],[0,-1],[0,+1]]
    for pos in last_pos:
        for move in l_move:
            x = pos.x + move[0]
            y = pos.y + move[1] 
            if check_pos(c_map, x, y):
                add_pos(n_pos, mapPos(x, y), previous)     
    return n_pos

def count_pos(d_pos):
    count = 0
    for x in d_pos:
        for y in d_pos[x]:
            count += 1
    return count

def main():
    c_map, start = read_map('input.txt')
    height = len(c_map)
    width = len(c_map[0])
    print(f"Size Map: {width}x{height}")
    
    new_pos = [start]
    odd_pos  = {}
    even_pos = {start.x:{start.y:True}}

    
    positions = [even_pos, odd_pos]
    
    repetition = max(width, height)
    repetition = repetition if repetition%2 == 0 else repetition*2
    
    ite = 0
    new_loop = []
    frec_news = [0]*repetition
    loop_rep = None
    while (loop_rep != new_loop):
        loop_rep = new_loop
        new_loop = []
        new_frec = []
        for i in range(1, 1+repetition):
            new_pos = move(c_map, new_pos, positions[i%2])
            new_frec.append(len(new_pos))
        
        for current, before in zip(new_frec, frec_news):
            new_loop.append(current-before)
        frec_news = new_frec
        ite += 1
        
    print(loop_rep)
    print(frec_news)
    
    steps = ite*repetition
    odd_count = count_pos(odd_pos)
    even_count = count_pos(even_pos)
    counts = [even_count, odd_count]
    for i in range(steps+1, 26501365+1):
        mod = (i-1)%repetition
        rep = (i-1-steps)//repetition
        rep += 1
        counts[i%2] += frec_news[mod] + loop_rep[mod] * rep
    
    print(mod, rep, i, counts[i%2])

            

        
    
main()