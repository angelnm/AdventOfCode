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
            if data == '#' or data == '.':
                block = Block(2*x, y, data)
                row.append(block)
                block = Block(2*x+1, y, data)
                row.append(block)
            elif data == '@':
                block = Block(2*x, y, data)
                row.append(block)
                user = block
                block = Block(2*x+1, y, '.')
                row.append(block)
            elif data == 'O':
                block = Block(2*x, y, '[')
                row.append(block)
                block = Block(2*x+1, y, ']')
                row.append(block)
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
        #for row in c_map:
        #    res = ""
        #    for b in row:
        #        res += f"{b}"
        #    print(res)
        
        
        x = user.x + MOVES[m][0]
        y = user.y + MOVES[m][1]
        
        block = c_map[y][x]
        if  block.data == '#':
            continue
        
        if block.data == '.':
            swap(c_map, user.x, user.y, x, y)
            continue
        
        if m == LEFT or m == RIGHT: 
            new_x = x
            while block.data == '[' or block.data == ']':
                new_x += MOVES[m][0]
                block = c_map[y][new_x]
            if block.data != '#':
                for new_x in range(new_x, x-MOVES[m][0], -MOVES[m][0]):
                    swap(c_map, new_x, y, new_x-MOVES[m][0], y)
        else:
            to_check = [c_map[user.y][user.x]]
            #side = c_map[y][x+1] if block.data == '[' else c_map[y][x-1]
            #to_check.append(side)
            
            cont = 0
            possible = True
            while cont<len(to_check) and possible:
                pos = to_check[cont]
                
                new_x = pos.x + MOVES[m][0]
                new_y = pos.y + MOVES[m][1]
                pos = c_map[new_y][new_x]
                
                if pos.data == '#':
                    possible = False
                    continue
                if pos.data == '[' or pos.data == ']':
                    if pos not in to_check:
                        to_check.append(pos)
                    pos = c_map[new_y][new_x+1] if pos.data == '[' else c_map[new_y][new_x-1]
                    if pos not in to_check:
                        to_check.append(pos)
                cont += 1
                
            if possible:
                cont = 0
                while to_check:
                    pos = to_check[cont]
                    
                    new_x = pos.x + MOVES[m][0]
                    new_y = pos.y + MOVES[m][1]
                    new_pos = c_map[new_y][new_x]
                    
                    if new_pos.data == '.':
                        swap(c_map, pos.x, pos.y, new_x, new_y)
                        to_check.remove(pos)
                    
                    cont += 1
                    if cont >= len(to_check):
                        cont =0
                    
def points(c_map):
    total = 0
    for row in c_map:
        for block in row:
            if block.data == '[':
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