WIDTH = 71
HEIGHT = 71
END = [WIDTH-1, HEIGHT-1]

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

def travel_map(c_map, end):
    start = [0,0]
    positions = [start]
    c_map[0][0] = 0
    
    cont = 0
    while positions and cont<len(positions):
        c_pos = positions[cont]
        c_x = c_pos[0]
        c_y = c_pos[1]
        
        if c_x == end[0] and c_y == end[1]:
            positions.append(end)
            return positions
        
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
            if m_steps == '.':
                c_map[y][x] = steps +1
                positions.append([x, y])
                continue
        cont += 1
    return positions
                
      

def main():
    c_bytes = read_bytes('input2.txt')
    
    n = 0
    c_map = generate_map(c_bytes, n)
    path = travel_map(c_map,END)
    while path[-1] == END:
        b = c_bytes[n]
        n += 1
        
        if b in path:
            c_map = generate_map(c_bytes, n)
            path = travel_map(c_map, END)
        
    print(c_bytes[n-1])
    c_map = generate_map(c_bytes, n)
    for l in c_map:
        print(*l, sep="")
    #print(c_map[70][70])

main()