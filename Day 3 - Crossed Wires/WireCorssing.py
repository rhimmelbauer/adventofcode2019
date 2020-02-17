from collections import namedtuple

class Movement():
    def __init__(self, step):
        self.step = step
        self.Direction = step[0]
        self.Hop = int(step[1:])
    
    def __repr__(self):
        return "Step: {}, Direction: {}, Hops: {}".format(self.step,self.Direction,self.Hop)

class WirePath():
    def __init__(self, pathSteps):
        self.Movements = []
        self.Coordinates = []
        for step in pathSteps:
            self.Movements.append(Movement(step))
        
        x = 0
        y = 0
        space = namedtuple('space','x y')

        self.Coordinates.append(space(x,y))
        for move in self.Movements:
            if move.Direction == 'R':
                for step in range(move.Hop):
                    x += 1
                    self.Coordinates.append(space(x,y))
            if move.Direction == 'L':
                for step in range(move.Hop):
                    x -= 1
                    self.Coordinates.append(space(x,y))
            
            if move.Direction == 'U':
                for step in range(move.Hop):
                    y += 1
                    self.Coordinates.append(space(x,y))
            if move.Direction == 'D':
                for step in range(move.Hop):
                    y -= 1
                    self.Coordinates.append(space(x,y))

    
    def PrintMovements(self):
        for step in self.Movements:
            print(step)

def readInput(filePath):
    file = open(filePath,'r')
    data = file.read().split(',')
    return data
    
wireA = "WireA.txt"
filePathB = "WireB.txt"
testWireA = "TestWireA.txt"
testWireB = "TestWireB.txt"

if __name__ == "__main__":
    WireA = WirePath(readInput(testWireA))
    WireB = WirePath(readInput(testWireB))
    diff = []
    for spaceA in WireA.Coordinates:
        for spaceB in WireB.Coordinates:
            if spaceA == spaceB:
                print("Same Space: {}".format(spaceB))
                diff.append(abs(spaceA.x + spaceA.y))
    print(diff)
    diff.pop(0)
    print("Min Cross Section Distance: {}".format(min(diff)))
    #for space in WireA.Coordinates:
    #WireA.PrintMovements()
    ## Draw WireA Path
    ## Draw WireB
    ### Check Crossing
    ## Calculate Distance from Registered Crossing points. 
