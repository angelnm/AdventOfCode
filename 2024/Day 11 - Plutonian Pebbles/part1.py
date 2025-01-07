class Rock:
    def __init__(self, value):
        self.value = value
     
    def blink(self):
        res = [self]
        value_str = str(self.value)
        
        if self.value == 0:
            self.value = 1
        elif len(value_str) % 2 == 0:
            mid = len(value_str)//2
            self.value = int(value_str[:mid])
            res.append(Rock(int(value_str[mid:])))
        else:
            self.value *= 2024
        return res
        
    def __repr__(self):
        return f"{self.value}"

def read_file(nameFile):
    file = open(nameFile, 'r')
    line = file.readline()
    file.close()
    
    rocks = []
    for rock in line.split():
        rock = int(rock)
        rocks.append(Rock(rock))
        
    return rocks

def blink(rocks):
    n_rocks = []
    for rock in rocks:
        n_rocks.extend(rock.blink())
    
    return n_rocks

def main():
    rocks = read_file('input1.txt')
    
    print(rocks)
    for i in range(75):
        rocks = blink(rocks)
        print(i)
        #print(rocks)
    print(len(rocks))
    
main()