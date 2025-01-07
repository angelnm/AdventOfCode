WIDTH  = 101
HEIGHT = 103

class Robot:
    def __init__(self, posX, posY, velX, velY):
        self.posX = posX
        self.posY = posY
        self.velX = velX
        self.velY = velY
        
    def time(self, seconds):
        self.posX += self.velX * seconds
        self.posX = self.posX % WIDTH
        
        self.posY += self.velY * seconds
        self.posY = self.posY % HEIGHT
     
    def cuadrant(self):        
        middleX = int(WIDTH/2)
        x = self.posX - middleX
        if WIDTH%2!=0 and x==0:
            return -1
        x = 0 if x<0 else 1
        
        middleY = int(HEIGHT/2)
        y = self.posY - middleY
        if HEIGHT%2!=0 and y==0:
            return -1
        y = 0 if y<0 else 1
        
        return x + y*2
        
    def __repr__(self):
        return f"({self.posX} {self.posY})"

def read_file(nameFile):
    file = open(nameFile, 'r')
    lines = file.read().split('\n')
    
    robots = []
    for line in lines:
        pos, vel = line.split()
        
        pos = pos.lstrip('p=')
        posX, posY = pos.split(',')
        posX = int(posX)
        posY = int(posY)
        
        vel = vel.lstrip('v=')
        velX, velY = vel.split(',')
        velX = int(velX)
        velY = int(velY)
        
        n_robot = Robot(posX, posY, velX, velY)
        robots.append(n_robot)
    return robots

def elapse_time(robots, seconds):
    for robot in robots:
        robot.time(seconds)

def safety_factor(robots):
    count = [0]*4
    for robot in robots:
        cuadrant = robot.cuadrant()
        print(robot, cuadrant)
        if cuadrant == -1:
            continue
        count[cuadrant] += 1
    
    factor = 1
    for c in count:
        factor*=c
    return factor

def print_robots(robots):
    c_map = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append(0)
        c_map.append(row)
        
    for row in c_map:
        res = ""
        for data in row:
            if data == 0:
                res += '.'
            else:
                res += '#'
        print(res)

def main():
    robots = read_file('input1.txt')
    elapse_time(robots, 100)
    factor = safety_factor(robots)
    print(factor)

main()