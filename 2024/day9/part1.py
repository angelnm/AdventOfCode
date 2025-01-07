def read_file(fileName):
    file = open(fileName, 'r')
    line = file.readline()
    file.close()
    
    return line

def read_disk(line):
    line = [int(x) for x in line]
    
    disk = []
    c_id = 0
    content = True
    for data in line:
        if content:
            disk.extend([c_id] * data)
            c_id += 1
            content = not content
        elif not content:
            disk.extend( [-1]* data)
            content = not content
    return disk

def compact_disk(disk):
    new_disk = [-1]*len(disk)
    
    i = 0
    j = len(disk)-1
    while i<=j:
        data = disk[i]
        
        if data == -1:
            data = disk[j]
            j -= 1
            while disk[j] == -1:
                j -= 1
            
        new_disk[i] = data
        i+=1
        
    return new_disk
    

def show_disk(disk):
    res = ""
    for data in disk:
        if data == -1:
            data = "."
        res += str(data)
    print(res)

def check_sum(disk):
    total = 0
    for idx, data in enumerate(disk):
        if data == -1:
            continue
        total += idx*data
    print(total)

def main():
    disk = read_file('input1.txt')
    disk = read_disk(disk)
    disk = compact_disk(disk)
    check_sum(disk)

main()