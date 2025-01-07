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
    if y<0 or y>=len(c_map):
        return False
    if x<0 or x>=len(c_map[0]):
        return False
    if c_map[y][x] == char:
        return True
    return False
 
def add_pos(l_pos, pos, v_map):
    if v_map[pos.y][pos.x] == 0:
        v_map[pos.y][pos.x] = 1
        l_pos.append(pos)

def visited_map(c_map):
    v_map = []
    for i in c_map:
        v_map.append([0]*len(i))
    return v_map

def move(c_map, l_pos):
    n_pos = []
    
    v_map = visited_map(c_map)
    l_move  = [[-1,0],[+1,0],[0,-1],[0,+1]]
    for pos in l_pos:
        for move in l_move:
            x = pos.x + move[0]
            y = pos.y + move[1]
            if check_pos(c_map, x, y):
                add_pos(n_pos, mapPos(x, y), v_map)
        
    return n_pos

def main():
    c_map, start = read_map('input.txt')
    
    l_pos = [start]
    for i in range(64):
        l_pos = move(c_map, l_pos)
    print(len(l_pos))
    
main()