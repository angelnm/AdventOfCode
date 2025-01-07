class Cell:
    def __init__(self, number):
        self.number = number
        self.after = []
        self.before = []
        
    def add_after(self, after):
        self.after.append(after.number)
        
    def add_before(self, before):
        self.before.append(before.number)
        
    def check_before(self, list_before):
        for i in list_before:
            if i in self.after:
                print('A')
                return False
        return True
        
    def check_after(self, list_after):
        for i in list_after:
            if i in self.before:
                return False
        return True
    
    def __repr__(self):
        res = f'{self.number} | {[x for x in self.before]} {[x for x in self.after]}'
        return res

def add_rule(before, after, cells):
    if (before not in cells):
        cells[before] = Cell(before)
    before = cells[before]
        
    if (after not in cells):
        cells[after] = Cell(after)
    after = cells[after]
        
    after.add_before(before)
    before.add_after(after)
    

def read_file(nameFile):
    file = open(nameFile, 'r')
    
    rules = []
    for line in file:
        line = line.strip('\n')
        if line == "":
            break
        rules.append(line)
    
    cells = {}
    for rule in rules:
        before, after = rule.split('|')
        add_rule(before, after, cells)
    
    pages = []
    for line in file:
        line = line.strip('\n')
        numbers = line.split(',')
        pages.append(numbers)
    
    file.close()
    return cells, pages

def check_page(cells, page):
    for idx, p in enumerate(page):
        cell = cells[p]
        before = page[:idx]
        after  = page[idx+1:]
    
        if ( (not cell.check_before(before)) or (not cell.check_after(after)) ):
            return False
    return True
    
def main():
    cells, pages = read_file('input1.txt')
        
    total_sum = 0
    for page in pages:
        if check_page(cells, page):
            middle = int(page[(len(page)//2)])
            total_sum += middle
    print(total_sum)
    
main()