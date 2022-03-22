from point import Point
from triangle import Triangle
from ploting import PlotPoints, PlotTriangles, PlotConnectedPoints
import math


def OrderPoints(points):
    """
    Orders points by x coordinate, if x coordinate is the same orders by y
    """
    #TODO Implement it
    raise NotImplementedError("Not yet implemented")

def RecursiveDivide(points):
    """
    Divides points in halfes until we have only 3 or 2 points in our array
    """

    if len(points) == 2:
        #we just connect two points together
        points[0].AddConnection(points[1])
        points[1].AddConnection(points[0])
        return
    
    if len(points) == 3:
        for i in range(3):
            points[i].AddConnection(points[i + 1 if i < 2 else 0])
            points[i].AddConnection(points[i + 2 if i < 1 else i - 1])
        return
    else:
        #we divide in half, first half will be bigger if odd number
        n = math.ceil(len(points) / 2)
        RecursiveDivide(points[0:n])
        RecursiveDivide(points[n:])



testne_tocke = list()

testne_tocke.append(Point(1, 2))
testne_tocke.append(Point(2, 1))
testne_tocke.append(Point(2, 3))
testne_tocke.append(Point(2, 4))
testne_tocke.append(Point(3, 2))
testne_tocke.append(Point(4, 4))
testne_tocke.append(Point(5, 3))
testne_tocke.append(Point(6, 1))
testne_tocke.append(Point(6, 2))
testne_tocke.append(Point(6, 4))

#PlotPoints(testne_tocke)

RecursiveDivide(testne_tocke)
for tocka in testne_tocke:
    print(tocka.connections)

PlotConnectedPoints(testne_tocke)
