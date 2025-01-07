def is_safe(report):    
    first = report[0]
    for idx in range(len(report)-1):
        if report[idx+1] < report[idx]:
            report.reverse()
            break
        elif report[idx+1] > report[idx]:
            break

    first = report[0]
    for value in report[1:]:
        dist = value - first
        if dist <= 0 or dist > 3:
            return False
        first = value
        
    return True

def check_report(report):
    report = report.split()
    report = [int(x) for x in report]
        
    safe = is_safe(report)
    if safe:
        return True
    
    for idx in range( len(report) ):
        c_report = report[:idx] + report[idx+1:]
        safe = is_safe(c_report)
        if safe:
            return True
    return False


def read_file():
    file = open('input2.txt', 'r')
    
    count = 0
    for report in file:
        isSafe = check_report(report)
        if isSafe:
            count += 1
    print(count)

def main():
    read_file()

main()