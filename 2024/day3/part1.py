def read_number(line, pos):
    number = ""
    n_line = len(line)
    while(pos < n_line and "0"<=line[pos]<="9"):
        number += line[pos]
        pos +=1
    return pos, int(number)

def process_data(line):
    total = 0
    
    pos = 0
    n_line = len(line)
    while(pos < n_line):
        if not line[pos:pos+4] == "mul(":
            pos += 1
            continue 
        pos, number1 = read_number(line, pos+4)
        if not line[pos] == ",":
            pos += 1
            continue
        pos, number2 = read_number(line, pos+1)
        if not line[pos] == ")":
            pos += 1
            continue
        mult = number1*number2
        total += mult
    return total
        

def read_file():
    file = open('input1.txt', 'r')
    
    instruction = ""
    for line in file:
        instruction += line
    
    return instruction

def main():
    instruction = read_file()
    
    total = process_data(instruction)
    print(total)

main()