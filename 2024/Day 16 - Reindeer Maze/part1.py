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
        
        self.min = math.inf
        
        
    def __repr__(self):
        return f"{self.data} {self.min}"
       
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
        current = path.pop(0)
        
        tile = current[0]
        score = current[1]
        c_dir = current[2]

        if score < tile.min:
            tile.min = score
            
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
            
            new_score = score+CST_M if n_dir==c_dir else score+CST_T+CST_M
            #if new_tile.min - new_score < -(CST_T+CST_M):
            #    continue
            if new_score > new_tile.min:
                continue
            if new_score > end.min:
                continue
            
            path.append([new_tile, new_score, n_dir, get_heur(new_tile, end)])
            path = sorted(path, key=lambda tile: tile[3])
            

def main():
    c_map, start, end = read_map('input1.txt')
    travel_map(c_map, start, end)
    print(end)
    
main()