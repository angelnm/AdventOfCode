def perform_operation(nums, operations):
    total = nums[0]
    for num, ope in zip(nums[1:], operations):
        if ope == 0:
            total += num
        elif ope == 1:
            total *= num
        else:
            tmp = f"{total}{num}"
            total = int(tmp)
    return total
    

def check_operation(total, nums):
    #print(total, nums)
    operations = [0]*(len(nums)-1)
    while operations != [2]*(len(nums)-1):
        ope = perform_operation(nums, operations)
        if ope == total:
            return True
        #print(operations)
        next_operation(operations)
        
    ope = perform_operation(nums, operations)
    if ope == total:
        return True   
    return False

def next_operation(operation):  
    for i in reversed(range(len(operation))):
        num = operation[i]
        if num != 2:
            operation[i] += 1
            break    
           
    for j in range(i+1, len(operation)):
        operation[j] = 0
    

def read_file(fileName):
    file = open(fileName, 'r')
    lines = file.read().split('\n')
    file.close()
    
    sum_total = 0
    for idx, line in enumerate(lines):
        #print(idx, line)
        total, nums = line.split(':')
        
        total = int(total)
        nums = nums.split()
        nums = [int(x) for x in nums]

        if check_operation(total, nums):
            sum_total += total
    print(sum_total)

def main():
    read_file('input2.txt')

main()