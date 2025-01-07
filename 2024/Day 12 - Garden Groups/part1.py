class Plant:
    def __init__(self, x, y, plant):
        self.x = x
        self.y = y
        self.plant = plant
        
        self.region = -1
        self.border = 0

class Map:
    def __init__(self, fileName):
        self.map = []
        self.regions = []
        
        self.read_map(fileName)
        self.search_regions()
        
    def read_map(self, fileName):
        file = open(fileName, 'r')
        
        for y, row in enumerate(file):
            row = row.rstrip('\n')
            row_plant = []
            self.map.append(row_plant)
            for x, value in enumerate(row):
                plant = self.create_plant(value, x, y)
                row_plant.append(plant)
    
    def set_region(self, plant, region):
        plant.region = region
        self.regions[region][1]+=1
        
        moves = [[+1,  0],
                 [-1,  0],
                 [ 0, +1],
                 [ 0, -1]]
        for m in moves:
            x = plant.x + m[0]
            y = plant.y + m[1]
            if y<0 or y>=len(self.map):
                plant.border += 1
                continue
            if x<0 or x>=len(self.map[0]):
                plant.border += 1
                continue
            
            new_plant = self.map[y][x]
            if new_plant.plant != plant.plant:
                plant.border += 1
                continue
            if  new_plant.region != -1:
                continue
            self.set_region(new_plant, region)

    
    def search_regions(self):
        for row in self.map:
            for plant in row:
                if plant.region != -1:
                    continue
                region = len(self.regions)
                self.regions.append([region,0])
                self.set_region(plant, region)
    
    def create_plant(self, value, x, y):
        plant = Plant(x, y, value)
        return plant
    
    def compute_price(self):
        total = 0
        for row in self.map:
            for plant in row:
                region = plant.region
                total += plant.border*self.regions[region][1]
        return total
                
    def __repr__(self):
        res = ""
        for row in self.map:
            for plant in row:
                res += str(plant.region)
            res += '\n'
        return res
                

def main():
    c_map = Map('input1.txt')
    total = c_map.compute_price()
    print(total)
main()