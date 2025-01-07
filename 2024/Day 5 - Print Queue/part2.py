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
        for idx, i in enumerate(list_before):
            if i in self.after:
                return idx
        return -1
        
    def check_after(self, list_after):
        for idx, i in enumerate(list_after):
            if i in self.before:
                return idx
        return -1
    
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

def check_page(cells, page, idx=0):
    for idx, p in enumerate(page[idx:]):
        cell = cells[p]
        before = page[:idx]
        after  = page[idx+1:]
    
        error_pos = cell.check_before(before)
        if ( error_pos != -1 ):
            number = page.pop(error_pos)
            page.insert(idx+1, number)
            return False, idx
        
        error_pos = cell.check_after(after)
        if( error_pos != -1 ):
            number = page.pop(idx+1+error_pos)
            page.insert(idx, number)
            return False, idx
    return True, 0
    
def main():
    cells, pages = read_file('input2.txt')
        
    total_sum = 0
    for page in pages:
        correct, pos = check_page(cells, page)
        if correct:
            continue
        
        while not correct:
            correct, pos = check_page(cells, page, pos)
            
        middle = int(page[(len(page)//2)])
        total_sum += middle
    print(total_sum)
    
main()