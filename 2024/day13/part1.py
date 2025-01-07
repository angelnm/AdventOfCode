Y = 1
X = 0

import numpy as np
def equation(buttonA, buttonB, prize):
    buttonA = np.array(buttonA)
    buttonB = np.array(buttonB)
    prize = np.array(prize)
    
    a = prize[Y]
    b = (prize[X]*buttonA[Y])/buttonA[X]
    c = buttonB[Y] - ((buttonB[X]*buttonA[Y])/buttonA[X])
       
    times_b = (a - b) / c  
    times_a = (prize[X] - times_b*buttonB[X]) / buttonA[X]
    
    s = np.array(times_a, times_b)
    if np.all(np.abs(s - np.round(s)) < 1e-3):
        return np.round(3*times_a + times_b)
    
    if int(times_b) == times_b and int(times_a) == times_a:
        return np.round(3*times_a + times_b)
    
    return 0



def process_button(line):
    _, data = line.split(':')
    a, b = data.split(',')
    
    a = a.lstrip(' X+')
    a = int(a)
    
    b = b.lstrip(' Y+')
    b = int(b)
    
    return a, b

def process_prize(line):
    _, data = line.split(':')
    a, b = data.split(',')
    
    a = a.lstrip(' X=')
    a = int(a)
    
    b = b.lstrip(' Y=')
    b = int(b)
    
    return a, b
    
def main():
    file = open('input1.txt', 'r')
    lines = file.read().split('\n')
    
    total = 0
    cont = 0
    while cont<len(lines):
        a, b = process_button(lines[cont])
        button_a = [a, b]
        a, b = process_button(lines[cont+1])
        button_b = [a, b]
        a, b = process_prize(lines[cont+2])
        prize = [a, b]             
        cont += 4
              
        total += equation(button_a, button_b, prize)

    print(total)

main()
