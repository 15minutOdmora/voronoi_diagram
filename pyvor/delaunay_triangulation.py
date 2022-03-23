from cgi import test
from sys import api_version
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

def CheckIfIntersects(point1, point2, point3, point4):
    """
    Check if line from point1 to point2 intersects with line from point3 to point4
    """
    x1, y1 = point1.GetCoords()
    x2, y2 = point2.GetCoords()
    x3, y3 = point3.GetCoords()
    x4, y4 = point4.GetCoords()

    #missing check if one line is on another!!!
    d = ((y2 - y1) * (x3 - x4) - (x2 - x1) * (y3 - y4))
    if d == 0:
        #Intersection doesnt exist
        return False

    alpha = ((y3 - y4) * (x1 - x3) - (x3 - x4) * (y1 - y3)) / d

    beta = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / d
    return 0 < alpha < 1 and 0 < beta < 1

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
        #LL
        left_cell = points[0:n]
        #RR
        right_cell = points[n:]

        #Recursively divide and connect when only 2 or 3 points
        RecursiveDivide(left_cell)
        RecursiveDivide(right_cell)






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

print(CheckIfIntersects(Point(1, 1), Point(1, 4), Point(1, 2), Point(1, 3)))

RecursiveDivide(testne_tocke)

PlotConnectedPoints(testne_tocke)
