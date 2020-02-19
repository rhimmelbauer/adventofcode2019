from collections import namedtuple
import os

BASE_PATH = "./Day 3 - Crossed Wires/"

WireA = BASE_PATH + "WireA.txt"
WireB = BASE_PATH + "WireB.txt"
TestWireA = BASE_PATH + "TestWireA.txt"
TestWireB = BASE_PATH + "TestWireB.txt"

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

def ReadInput(filePath):
    file = open(filePath,'r')
    data = file.read().split(',')
    return data
    


if __name__ == "__main__":
    print("Working on dir: {}".format(os.getcwd()))
    WireA = WirePath(ReadInput(WireA))
    WireB = WirePath(ReadInput(WireB))
    distancesFromOrigin = []
    crossSectionIndexes = []
    crossSectionsWireLength = []
    for spaceA in WireA.Coordinates:
        try:
            wireBIndex = WireB.Coordinates.index(spaceA)
            wireAIndex = WireA.Coordinates.index(spaceA)
            crossSectionIndexes.append([wireAIndex,wireBIndex])
            totalWireLengthPath = wireAIndex + wireBIndex
            crossSectionsWireLength.append(totalWireLengthPath)
            differenceFromOrigin = (abs(spaceA.x) + abs(spaceA.y))
            print("Same Space: {} , Distance: {}, Wire A Length: {}, Wire B Length: {}, Total Length: {}".format(spaceA, differenceFromOrigin, wireAIndex, wireBIndex, totalWireLengthPath))
            distancesFromOrigin.append(differenceFromOrigin)
        except:
            pass
    print("Distances from Origin: {}".format(distancesFromOrigin))
    print("Total Lengths from cross section: {}".format(crossSectionsWireLength))
    distancesFromOrigin.pop(0)
    print("Min Cross Section Distance: {}".format(min(distancesFromOrigin)))
    crossSectionsWireLength.pop(0)
    print("Min Wire Length: {}".format(min(crossSectionsWireLength)))
    #for space in WireA.Coordinates:
    #WireA.PrintMovements()
    ## Draw WireA Path
    ## Draw WireB
    ### Check Crossing
    ## Calculate Distance from Registered Crossing points. 
