
class Cell:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.parents = []

    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)

    def count_path(self):
        if self.height == 9:
            return [self]
        
        total = []
        for cell in self.parents:
            current = cell.count_path()
            for c in current:
                if c not in total:
                    total.append(c)
        return total
        
    def __repr__(self):
        return f"({self.height} {len(self.parents)})"

def read_map(fileName):
    file = open(fileName, 'r')
    lines = file.read().split('\n')
    file.close()
    
    c_map = []
    c_top = []
    c_low = []
    for y, line in enumerate(lines):
        c_row = []
        for x, data in enumerate(line):
            data = int(data)
            c_cell = Cell(x, y, data)
            c_row.append(c_cell)
            if data == 9:
                c_top.append(c_cell)
            if data == 0:
                c_low.append(c_cell)
        c_map.append(c_row)
        
    return c_map, c_top, c_low

def show_map(c_map):
    for row in c_map:
        cadena = ""
        for cell in row:
            cadena += str(cell)
        print(cadena)

def process_layer(c_map, c_layer):
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    n_layer = []
    
    while (c_layer):
        c_cell = c_layer.pop()
        c_x = c_cell.x
        c_y = c_cell.y
        c_h = c_cell.height
        
        for x, y in move:
            x += c_x
            y += c_y
            
            if x<0 or x>=len(c_map[0]):
                continue
            if y<0 or y>=len(c_map):
                continue
            next_cell = c_map[y][x]
            if next_cell.height != c_h-1:
                continue
            if not next_cell.parents:
                n_layer.append(next_cell)
            next_cell.add_parent(c_cell)
    return n_layer
    
    

def process_map(c_map, c_top):
    while(c_top):
        c_top = process_layer(c_map, c_top)
    
def main():
    c_map, c_top, c_low = read_map('input1.txt')
    process_map(c_map, c_top)
    
    total = 0
    for c in c_low:
        total_ends = c.count_path()
        total += len(total_ends)
    print(total)

main()