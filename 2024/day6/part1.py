TOP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Guard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = TOP
    
    def move1step(self, c_map):
        move = self.getMove()
        x = self.x + move[0]
        y = self.y + move[1]
        
        if y<0 or y>=len(c_map):
            return False
        if x<0 or x>=len(c_map[0]):
            return False
        
        if c_map[y][x] == '#':
            self.turnGuard()
            return True
        
        self.x = x
        self.y = y
        
        return True
    
    def turnGuard(self):
        self.dir = (self.dir+1)%4
    
    def getMove(self):
        if self.dir == TOP:
            return [0, -1]
        elif self.dir == RIGHT:
            return [+1, 0]
        elif self.dir == DOWN:
            return [0, +1]
        else:
            return [-1, 0]
    
    def __repr__(self):
        return f'({self.x} {self.y} | {self.dir})'
        
      
def read_map(fileName):
    file = open(fileName, 'r')
    lines = file.read().split('\n')
    file.close()

    c_map = []
    c_guard = None
    for y, line in enumerate(lines):
        
        if '^' in line:
            n_line = ''
            for x,char in enumerate(line):
                if char != '^':
                    n_line += char
                else:
                    n_line += '.'
                    c_guard = Guard(x, y)       
            line = n_line
        c_map.append(line)
                
    return c_map, c_guard   
 
def add_position(dic_pos, guard):
    x = guard.x
    y = guard.y
    direction = guard.dir
    
    if x not in dic_pos:
        dic_pos[x] = {}
    if y not in dic_pos[x]:
        dic_pos[x][y] = []
    if direction not in dic_pos[x][y]:
        dic_pos[x][y].append(direction)
        return True
    return False

def count_positions(dic_pos):
    count = 0
    for x in dic_pos:
        count += len(dic_pos[x])
    return count

def main():
    c_map, guard = read_map('input1.txt')
    
    guard_positions = {}
    added = add_position(guard_positions, guard)
    while( guard.move1step(c_map) and added):
        added = add_position(guard_positions, guard)
        
    print(count_positions(guard_positions))

main()