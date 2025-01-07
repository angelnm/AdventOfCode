
def read_file(nameFile):
    file = open(nameFile, 'r')
    towels_file, patterns_file = file.read().split('\n\n')
    
    towels = []
    max_width = 0
    for line in towels_file.split(', '):
        towels.append(line)
        if len(line) > max_width:
            max_width = len(line)
    
    patterns = []
    for line in patterns_file.split('\n'):
        patterns.append(line)
        
    return towels, patterns, max_width
    
def isPossible(pattern, towels, max_t):
    options = [0] * (len(pattern)+1)
    
    options[0] = 1
    pos = 0
    
    while pos<len(options):
        c_times = options[pos]
        c_option = pattern[:pos]
       
        width = 1
        while pos+width <= len(pattern) and width<=max_t:
            if pattern[pos:pos+width] in towels:
                options[pos+width] += c_times
            width += 1
        pos += 1
    
    #print(options)
    return options[-1]
    
def main():
    towels, patterns, max_t = read_file('input2.txt')
    
    cont = 0
    for idx, p in enumerate(patterns):
        print(idx, len(patterns))
        n_combinations = isPossible(p, towels, max_t)
        cont += n_combinations
    print(cont)

main()