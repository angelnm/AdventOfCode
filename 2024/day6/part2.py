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
    
    def copy(self):
        return Guard(self.x, self.y)
    
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
        c_map.append(list(line))
                
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

def remove_position(dic_pos, x, y):
    if x in dic_pos:
        if y in dic_pos[x]:
            dic_pos[x].pop(y)

def count_positions(dic_pos):
    count = 0
    for x in dic_pos:
        count += len(dic_pos[x])
    return count

def check_map(c_map, guard):
    n_guard = guard.copy()
    
    guard_positions = {}
    added = add_position(guard_positions, n_guard)
    while( n_guard.move1step(c_map) and added):
        added = add_position(guard_positions, n_guard)
    
    return guard_positions, not added

def check_obstacle(c_map, guard, x, y):
    c_map[y][x] = '#'
    _, looped = check_map(c_map, guard)
    c_map[y][x] = '.'
    return looped

def main():
    c_map, guard = read_map('input2.txt')
    
    guard_positions, looped = check_map(c_map, guard)
    remove_position(guard_positions, guard.x, guard.y)
    
    total_obs = 0
    for x in guard_positions:
        for y in guard_positions[x]:
            looped = check_obstacle(c_map, guard, x, y)
            if looped:
                total_obs += 1
    print(total_obs)

main()