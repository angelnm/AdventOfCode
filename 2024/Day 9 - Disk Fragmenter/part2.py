class File:
    def __init__(self, data, space, pos):
        self.data = data
        self.space = space
        self.pos = pos
    
    def copy(self):
        return File(self.data, self.space, self.pos)
    
    def checksum(self, idx):
        total = 0
        if self.data == '.':
            return total
        for i in range(self.space):
            total += idx*self.data
            idx += 1
        return total
    
    def __lt__(self, obj):
        return ((self.pos) < (obj.pos))

    def __gt__(self, obj):
        return ((self.pos) > (obj.pos))

    def __le__(self, obj):
        return ((self.pos) <= (obj.pos))

    def __ge__(self, obj):
        return ((self.pos) >= (obj.pos))
    
    def __repr__(self):
        data = f"{str(self.data) * (self.space)}"
        if self.space == 0:
            data = "ERROR"
        return data

def read_file(fileName):
    file = open(fileName, 'r')
    line = file.readline()
    file.close()
    
    return line

def read_disk(line):
    line = [int(x) for x in line]
    
    disk = []
    files = []
    spaces = []
    for i in range(10):
        spaces.append([])

    c_id = 0
    c_pos = 0
    content = True
    for data in line:
        if content:
            content = not content
            if data != 0:
                file = File(c_id, data, c_pos)
                files.append(file)
                disk.append(file)
            c_id += 1
            c_pos += data
        elif not content:
            content = not content
            if data != 0:
                file = File(".", data, c_pos)
                disk.append(file)
                spaces[data].append(file)
            c_pos += data
    files.reverse()
    return disk, files, spaces

def compact_disk(disk, files, spaces):
    for file in files:
        file_space = file.space
        file_pos   = file.pos
        
        possible = []
        [possible.extend(x) for x in spaces[file_space:]]
        possible.sort()
        
        if not possible:
            continue
        
        space = possible[0]
        
        if space.pos >= file.pos:
            continue
        
        # Move File
        file.pos = space.pos
        # Move/Cut Space
        disk.append(File('.', file_space, file_pos))
        spaces[space.space].remove(space)
        space.space -= file_space
        space.pos += file_space
        if space.space<= 0:
            disk.remove(space)
        else:
            spaces[space.space].append(space)

                
    disk.sort()
    

def show_disk(disk):
    res = ""
    for data in disk:
        res += str(data)
    print(res)

def check_sum(disk):
    total = 0
    idx = 0
    for file in disk:
        total += file.checksum(idx)
        idx += file.space
    
    print(total)

def main():
    disk = read_file('input2.txt')
    disk, files, spaces = read_disk(disk)
    #show_disk(disk)
    compact_disk(disk, files, spaces)
    #show_disk(disk)
    check_sum(disk)
    #disk = compact_disk(disk)

main()