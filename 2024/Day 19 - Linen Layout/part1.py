
def read_file(nameFile):
    file = open(nameFile, 'r')
    towels_file, patterns_file = file.read().split('\n\n')
    
    towels = []
    for line in towels_file.split(', '):
        towels.append(line)
    
    patterns = []
    for line in patterns_file.split('\n'):
        patterns.append(line)
        
    return towels, patterns
    
def isPossible(pattern, towels):
    options = {'':0}
    
    while options:
        c_option = next(iter(options))
        pos = options.pop(c_option)
        if c_option == pattern:
            return True
        
        width = 1
        while pos+width <= len(pattern):
            if pattern[pos:pos+width] in towels:
                options[pattern[:pos+width]] = pos+width
            width += 1
    
def main():
    towels, patterns = read_file('input1.txt')
    
    cont = 0
    for p in patterns:
        if (isPossible(p, towels)):
            cont += 1
    print(cont)

main()