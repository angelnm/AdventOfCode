TOP = 0
RIGHT = 1
BOT = 2
LEFT = 3

MOVES = [[+0, -1],
         [+1, +0],
         [+0, +1],
         [-1, 0]]
        

class Block:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_pos(self):
        return [self.x, self.y]

    def __repr__(self):
        return f"{self.data}"

def read_file(fileName):
    file = open(fileName, 'r')
    
    lines = file.read()
    l_part1, l_part2 = lines.split('\n\n')

    c_map = []
    user = None
    for y, l in enumerate(l_part1.split('\n')):
        row = []
        for x, data in enumerate(l):
            block = Block(x, y, data)
            row.append(block)
            if data == '@':
                user = block
        c_map.append(row)
        
    moves = []
    for l in l_part2.split('\n'):
        for data in l:  
            if data == '^':
                moves.append(0)
            elif data == '>':
                moves.append(1)
            elif data =='v':
                moves.append(2)
            else:
                moves.append(3)

          
    return c_map, moves, user
        
def swap(c_map, x0, y0, x1, y1):
    tmp = c_map[y0][x0]
    c_map[y0][x0] = c_map[y1][x1]
    c_map[y1][x1] = tmp
    
    tmp = c_map[y0][x0].get_pos()
    c_map[y0][x0].set_pos(c_map[y1][x1].get_pos())
    c_map[y1][x1].set_pos(tmp)

def move(c_map, moves, user):
    for m in moves:     
        x = user.x + MOVES[m][0]
        y = user.y + MOVES[m][1]
        
        block = c_map[y][x]
        if  block.data == '#':
            continue
        
        if block.data == '.':
            swap(c_map, user.x, user.y, x, y)
            continue
        
        new_x = x
        new_y = y
        while block.data == 'O':
            new_x += MOVES[m][0]
            new_y += MOVES[m][1]
            block = c_map[new_y][new_x]
        if block.data == '#':
            continue
        swap(c_map, x, y, new_x, new_y)
        swap(c_map, user.x, user.y, x, y)


def points(c_map):
    total = 0
    for row in c_map:
        for block in row:
            if block.data == 'O':
                total += block.x + block.y*100
    return total

def main():
    c_map, moves, user = read_file('input1.txt')
    
    
    move(c_map, moves, user)
    total = points(c_map)
    print(total)
    
    for row in c_map:
        res = ""
        for b in row:
            res += f"{b}"
        print(res)

main()