def read_file(nameFile):
    file = open(nameFile, 'r')
    line = file.readline()
    file.close()
    
    rocks = {}
    for rock in line.split():
        rock = int(rock)
        if rock not in rocks:
            rocks[rock] = 0
        rocks[rock] += 1
        
    return rocks

def blink_rock(rock):
    res = []
    rock_str = str(rock)
        
    if rock == 0:
        res.append(1)
    elif len(rock_str) % 2 == 0:
        mid = len(rock_str)//2
        res.append( int(rock_str[:mid]) )
        res.append( int(rock_str[mid:]) )
    else:
        res.append(rock*2024)
        
    return res
    
def blink(rocks):
    n_rocks = {}
    for rock in rocks:
        times = rocks[rock]
        created = blink_rock(rock)
        
        for c in created:
            if c not in n_rocks:
                n_rocks[c] = 0
            n_rocks[c] += times
    
    return n_rocks

def count_rocks(rocks):
    total = 0
    for r in rocks:
        total += rocks[r]
    print(total)
        
def main():
    rocks = read_file('input2.txt')
    
    print(rocks)
    count_rocks(rocks)
    for i in range(75):
        rocks = blink(rocks)
        count_rocks(rocks)
    #print(len(rocks))
    
main()