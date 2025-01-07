class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getDif(self, other):
        return Pos(self.x - other.x, self.y - other.y)
    
    def mult(self, num):
        return Pos(self.x*num, self.y*num)
    
    def add(self, other):
        return Pos(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"({self.x} {self.y})"
        
    def __eq__(self, other):
        if isinstance(other, Pos):
            return (other.x == self.x and other.y == self.y)
        return False


def read_map(fileName):
    file = open(fileName, 'r')
    lines = file.read().split('\n')
    file.close()
    
    c_map = []
    c_ant = {}
    for y, line in enumerate(lines):
        c_map.append(line)
        for x, char in enumerate(line):
            if char != '.':
                if char not in c_ant:
                    c_ant[char] = []
                c_ant[char].append(Pos(x, y))
    return c_map, c_ant

def add_pos(pos, width, height, antinodes):
    if pos.x < 0 or pos.x >= width:
        return False
    if pos.y < 0 or pos.y >= height:
        return False
    if pos in antinodes:
        return True
    antinodes.append(pos)
    return True

def add_all_pos(start, dif, width, height, antinodes):
    while( add_pos(start, width, height, antinodes) ):
        start = start.add(dif)
    

def compute_antinodes(c_map, c_ant):
    width = len(c_map[0])
    height = len(c_map)
    
    antinodes = []
    for char in c_ant:
        l_pos = c_ant[char]
        for i in range( len(l_pos) ):
            for j in range( i+1, len(l_pos) ):
                first_pos = l_pos[i]
                secnd_pos = l_pos[j]
                dif_pos = first_pos.getDif(secnd_pos)
                
                add_all_pos(first_pos, dif_pos, width, height, antinodes)
                add_all_pos(secnd_pos, dif_pos.mult(-1), width, height, antinodes)
            
    return antinodes
                

def main():
    c_map, c_ant = read_map('input2.txt')
    for l in c_map:
        print(l)
    print()
    for char in c_ant:
        print(char, c_ant[char])
    print()
    antinodes = compute_antinodes(c_map, c_ant)
    print(len(antinodes))

main()