def read_file():
    file = open('input2.txt', 'r') 
    
    list1 = []
    dict1 = {}
    for line in file:
        id1, id2 = line.split()
        
        id1 = int(id1)        
        list1.append(id1)
        
        id2 = int(id2)
        if id2 not in dict1:
            dict1[id2] = 0
        dict1[id2] += 1
        
    
    file.close()
    return list1, dict1
        
    
def main():
    list1, dict1 = read_file()
    
    output = 0
    for n in list1:
        if n in dict1:
            output += n*dict1[n]
    print(output)

main()
