WIDTH = 71
HEIGHT = 71

MOVES = [[+0,-1],
         [+1,+0],
         [+0,+1],
         [-1,+0]]

def read_bytes(nameFile):
    file = open(nameFile, 'r')
    
    c_bytes = []
    for line in file:
        x, y = line.split(',')
        x = int(x)
        y = int(y)
        c_bytes.append([x, y])
    
    return c_bytes

def generate_map(c_bytes, steps):
    c_map = []
    for i in range(HEIGHT):
        c_map.append(['.']*WIDTH)
        
    for i in range(steps):
        byte = c_bytes[i]
        x = byte[0]
        y = byte[1]
        c_map[y][x] = '#'
    
    return c_map

def travel_map(c_map):
    start = [0,0]
    positions = [start]
    c_map[0][0] = 0
    while positions:
        c_pos = positions.pop(-1)
        c_x = c_pos[0]
        c_y = c_pos[1]
        steps = c_map[c_y][c_x]
        
        for m in MOVES:
            x = c_x + m[0]
            y = c_y + m[1]
            if y<0 or y>=len(c_map):
                continue
            if x<0 or x>=len(c_map[0]):
                continue
            
            m_steps = c_map[y][x]
            if m_steps == '#':
                continue
            if m_steps == '.' or  int(steps+1) < int(m_steps):
                c_map[y][x] = steps +1
                positions.append([x, y])
                continue
                
      

def main():
    c_bytes = read_bytes('input1.txt')
    c_map = generate_map(c_bytes, 1024)
    travel_map(c_map)
    
    for l in c_map:
        print(*l, sep="")
    print(c_map[70][70])

main()