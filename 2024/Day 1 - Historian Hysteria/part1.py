
def read_file():
    file = open('input1.txt', 'r') 
    
    list1 = []
    list2 = []
    for line in file:
        id1, id2 = line.split()
        list1.append(int(id1))
        list2.append(int(id2))
    
    file.close()
    return list1, list2
        
    
def main():
    list1, list2 = read_file()
    
    list1.sort()
    list2.sort()

    sum_dif = 0
    for a, b in zip(list1, list2):
        sum_dif += abs(a - b)
    print(sum_dif)
    
main()
