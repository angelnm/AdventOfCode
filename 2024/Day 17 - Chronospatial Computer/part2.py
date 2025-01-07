import math

class Program:
    def __init__(self, nameFile=""):
        self.reset_variables()
        if nameFile != "":
            self.read_program(nameFile)
        
    def read_program(self, nameFile):
        file = open(nameFile, 'r')
        registers, program = file.read().split('\n\n')
        
        registers = registers.split('\n')
        self.R_A = int(registers[0].split(':')[1])
        self.R_B = int(registers[1].split(':')[1])
        self.R_C = int(registers[2].split(':')[1])
        
        program = program.split(':')[1]
        self.PROGRAM = [int(x) for x in program.split(',')]
        
    def reset_variables(self):
        self.R_A = 0
        self.R_B = 0
        self.R_C = 0
        self.POINTER = 0
        self.PROGRAM = []
        self.OUT = []
    
    def copy(self):
        p = Program()
        p.R_A = self.R_A
        p.R_B = self.R_B
        p.R_C = self.R_C
        p.PROGRAM = self.PROGRAM
        return p
    
    def get_combo(self, value):
        if value<=3:
            return value
        elif value == 4:
            return self.R_A
        elif value == 5:
            return self.R_B
        elif value == 6:
            return self.R_C
        else:
            print('ERROR COMBO 7')
    
    def run_program(self):
        while(self.POINTER < len(self.PROGRAM)):
            instruction = self.PROGRAM[ self.POINTER ]
            operand = self.PROGRAM[ self.POINTER+1 ]
            
            if instruction == 0:
                den = self.get_combo(operand)
                res = self.R_A / math.pow(2,den)
                res = int(res)
                self.R_A = res
            elif instruction == 1:
                res = self.R_B ^ operand
                self.R_B = res
            elif instruction == 2:
                res = self.get_combo(operand)
                res = res % 8
                self.R_B = res
            elif instruction == 3:
                if self.R_A != 0:
                    self.POINTER = operand
                    continue
            elif instruction == 4:
                res = self.R_B ^ self.R_C
                self.R_B = res
            elif instruction == 5:
                res = self.get_combo(operand)
                res = res % 8
                self.OUT.append(res)
                if self.OUT[-1] != self.PROGRAM[len(self.OUT)-1]:
                    return
            elif instruction == 6:
                den = self.get_combo(operand)
                res = self.R_A / math.pow(2,den)
                res = int(res)
                self.R_B = res
            elif instruction == 7:
                den = self.get_combo(operand)
                res = self.R_A / math.pow(2,den)
                res = int(res)
                self.R_C = res
                  
            self.POINTER += 2
        print(*self.OUT, sep=',')
  
def get_possible(last_3):
    numbers = []
               
    for i in ['0','1']:
        if last_3[0] != '_':
            i = last_3[0]
        for j in ['0','1']:
            if last_3[1] != '_':
                j = last_3[1]
            for k in ['0','1']:
                if last_3[2] != '_':
                    k = last_3[2]
                new = [i, j, k]
                if new not in numbers:
                    numbers.append(new)
     
    return numbers    

def get_number(program):
    first = ['_']*((len(program)+10)*3)
    
    numbers = {''.join(first):[[], first]}
    while numbers:
        key = list(numbers.keys())[0]
        current = numbers.pop(key)
        
        pr = current[0]
        nb = current[1]
        
        if pr == program:
            break
        
        pos = len(pr)*3
        wanted = program[len(pr)]
        nb = current[1]
        #print(pos, pr, ''.join(nb))
        
        last3 = nb[-3-pos:-pos] if pos != 0 else nb[-3-pos:]
        #print(pos, last3)
        possible = get_possible(last3)
        #print(possible)
        for comb in possible: 
            toAdd = True
            
            move = int(''.join(comb), 2) ^1
            b = move^5
            move = pos+move
            c = b^wanted
            
            number = nb.copy()

            for idx, com in enumerate(comb):
                n = number[-1-pos-2+idx] 
                if n != '_' and n!= com:
                    toAdd = False
                    break
                number[-1-pos-2+idx] = com
  
            bin_c = list( bin(c)[2:])
            while len(bin_c) != 3:
                bin_c.insert(0, '0')
            for idx, com in enumerate( bin_c ):
                n = number[-1-move-2+idx] 
                if n != '_' and n!= com:
                    toAdd = False
                    break
                number[-1-move-2+idx] = com 
           
            if not toAdd:
                continue
            
            numbers[''.join(number)] = [pr + [wanted], number]
    
    nb = [x if x != '_' else '0' for x in nb]
    return nb
        
    
    
def main():
    program = Program('input1.txt')
    n = get_number(program.PROGRAM)
    program.R_A = int(''.join(n),2)
    print(program.R_A)
    program.run_program()

    
    
    # We are going to try for each one of the possible

    
    #print(CONT)

main()