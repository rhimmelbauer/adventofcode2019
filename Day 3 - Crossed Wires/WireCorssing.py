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

def readInput(filePath):
    file = open(filePath,'r')
    data = file.read().split(',')
    return data
    


if __name__ == "__main__":
    print("Working on dir: {}".format(os.getcwd()))
    WireA = WirePath(readInput(WireA))
    WireB = WirePath(readInput(WireB))
    distancesFromOrigin = []
    crossSectionIndexes = []
    crossSectionsWireLength = []
    o = [27726, 24752, 25018, 34482, 91744, 88346, 12936, 93100, 13588, 93100, 103932, 104964, 62774, 62890, 65384, 65384, 109252, 109612, 108292, 108832, 114712, 113110, 116094, 113784, 113784, 126648, 126990, 72202, 73068, 116004, 117300, 119868, 120014, 120460, 121222, 120346, 152852, 153480, 158918, 79718, 79580, 156474, 78262, 77574, 108936, 166338, 144794, 144794, 113642, 155712, 187280, 108156, 107942, 188878, 184664, 106408, 106408, 184664, 189710, 189710, 186924, 186924, 124964, 124964, 123876, 123876, 127900, 130936]
    print(min(o))
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
    #for space in WireA.Coordinates:
    #WireA.PrintMovements()
    ## Draw WireA Path
    ## Draw WireB
    ### Check Crossing
    ## Calculate Distance from Registered Crossing points. 
