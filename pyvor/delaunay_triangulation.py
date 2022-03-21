from point import Point
from triangle import Triangle
from ploting import PlotPoints, PlotTriangles


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
        points[0].AddConnection(points[1])
        points[0].AddConnection(points[1])



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

PlotPoints(testne_tocke)
