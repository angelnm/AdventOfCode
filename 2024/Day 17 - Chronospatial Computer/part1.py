import math

class Program:
    def __init__(self, nameFile):
        self.reset_variables()
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
        print(self.R_A, self.R_B, self.R_C)
        print(*self.OUT, sep=',')
  
def main():
    program = Program('input1.txt')
    program.run_program()

main()