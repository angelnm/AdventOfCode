import math

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

CST_M = 1
CST_T = 1000

MOVES = [[+0,-1],
         [+1,+0],
         [+0,+1],
         [-1,+0]]

class Block:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        
        self.min = [math.inf, math.inf, math.inf, math.inf]
        self.dir = [-1, -1, -1, -1]
        
    def check_min(self, scores, c_dir):
        some_improve = False
        for i in range(4):
             sc = scores[i]
             if sc < self.min[i]:
                 self.min[i] = sc
                 self.dir[i] = [c_dir]
                 some_improve = True
             elif sc == self.min[i]:
                self.dir[i].append(c_dir)
        return some_improve
        
    def __repr__(self):
        return f"{self.x} {self.y} {self.min} {self.dir}"
       
def read_map(nameFile):
    file = open(nameFile, 'r')
    lines = file.read().split('\n')
    
    c_map = []
    start = None
    end = None
    for y, line in enumerate(lines):
        row = []
        for x, data in enumerate(line):
            block = Block(x, y, data)
            row.append(block)
            if data == 'S':
                block.data = '.'
                start = block
            if data == 'E':
                block.data = '.'
                end = block
        c_map.append(row)

    return c_map, start, end

def get_heur(tile1, tile2):
    dist = 0
    dist += abs(tile2.x - tile1.x)*CST_T
    dist += abs(tile2.y - tile1.y)*CST_T
    
    #dist = math.pow(tile2.x-tile1.x, 2) + math.pow(tile2.y-tile1.y, 2)
    #dist = math.sqrt(dist)
    return dist

def travel_map(c_map, start, end):
    path = [[start, 0, 1, get_heur(start, end)]]
    
    while path:
        print(len(path))
        current = path.pop(0)
        
        tile = current[0]
        score = current[1]
        c_dir = current[2]

        scores = [0]*4
        scores[c_dir] = score
        scores[(c_dir+1)%4] = score+1000
        scores[(c_dir+2)%4] = score+2000
        scores[(c_dir+3)%4] = score+1000
        improvement = tile.check_min(scores, c_dir)
            
        if not improvement:
            continue
        
        #if tile == end:
        #   return
            
        for n_dir, m in enumerate(MOVES):
            x = tile.x + m[0]
            y = tile.y + m[1]
            
            new_tile = c_map[y][x]
            if new_tile.data == '#':
                continue
            if (n_dir+2)%4==c_dir:
                continue
            
            new_score = tile.min[n_dir] +1
            if new_score > new_tile.min[n_dir]:
                continue
            
            path.append([new_tile, new_score, n_dir, get_heur(new_tile, end)])
            path = sorted(path, key=lambda tile: tile[3])
            
def count_path(c_map, end, start):
    total = []
    path = []
    
    min_score = min(end.min)
    for idx, score in enumerate(end.min):
        if score == min_score:
            path.append([end, idx])
    
    while path:
        data = path.pop()
        current = data[0]
        dir_from = data[1]
        # print(current)
        
        if current not in total:
            total.append(current)
        else:
            continue
               
        if current == start:
            continue
        
        dirs = current.dir[dir_from]
        score = current.min[dir_from]

        for c_dir in dirs:   
            n_dir = (c_dir-2)%4
            x = current.x + MOVES[n_dir][0]
            y = current.y + MOVES[n_dir][1]
            path.append([c_map[y][x], c_dir])
            
            
def main():
    c_map, start, end = read_map('input2.txt')
    travel_map(c_map, start, end)
    #print(end)
    print("Start Count")
    count_path(c_map, end, start)
    
main()