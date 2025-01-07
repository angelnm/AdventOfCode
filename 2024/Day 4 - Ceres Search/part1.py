def read_file():
    file = open('input1.txt', 'r')
    
    matrix = []
    for line in file:
        matrix.append(line.strip('\n'))
    
    file.close()
    return matrix

def its_xmas(matrix, x, y, sumX, sumY):
    res = ""
    for i in range(4):
        idxY = y + sumY*i
        idxX = x + sumX*i
        
        if idxY<0 or idxY>=len(matrix):
            continue
        if idxX<0 or idxX>=len(matrix[idxY]):
            continue
        res += matrix[idxY][idxX]
     
    if res == "XMAS":
        return 1
    return 0

def search_xmas(matrix, x, y):
    total = 0
    # Search Right
    total += its_xmas(matrix, x, y,  1,  0)
    total += its_xmas(matrix, x, y, -1,  0)
    total += its_xmas(matrix, x, y,  0,  1)
    total += its_xmas(matrix, x, y,  0, -1)
    total += its_xmas(matrix, x, y,  1,  1)
    total += its_xmas(matrix, x, y,  1, -1)
    total += its_xmas(matrix, x, y, -1,  1)
    total += its_xmas(matrix, x, y, -1, -1)
    # Search Left
    return total

def process_data(matrix):
    total = 0
    for y, line in enumerate(matrix):
        for x, letter in enumerate(line):
            if letter == "X":
                total += search_xmas(matrix, x, y)
    return total

def main():
    matrix = read_file()
    times = process_data(matrix)
    print(times)
    
main()