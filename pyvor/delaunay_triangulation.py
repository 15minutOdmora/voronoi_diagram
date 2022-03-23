from cgitb import small
from operator import le
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


def AngleBetweenLines(point1, point2, point3, point4):
    """
    Calculates angle between line from point1 to point2 and point3 to point4
    """
    x1, y1 = point1.GetCoords()
    x2, y2 = point2.GetCoords()
    x3, y3 = point3.GetCoords()
    x4, y4 = point4.GetCoords()

    vector1 = (x2 - x1, y2 - y1)
    vector2 = (x4 - x3, y4 - y3)

    vector1_x_vector2 = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    vector1_norm = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
    vector2_norm = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

    return math.degrees(math.acos(vector1_x_vector2 / (vector1_norm * vector2_norm)))


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
        #Lines are paralel so only check if one is on another
        #find smaller one
        vector1 = (x2 - x1, y2 - y1)
        vector2 = (x4 - x3, y4 - y3)
        vector1_norm = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
        vector2_norm = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

        #take both point of smaller one and check if at least one is on the line
        if vector1_norm < vector2_norm:
            larger_vector = vector2
            larger_point = point3.GetCoords()
            points = [point1.GetCoords(), point2.GetCoords()]
        else:
            larger_vector = vector1
            larger_point = point1.GetCoords()
            points = [point3.GetCoords(), point4.GetCoords()]            
        
        #get k and n for larger vector y = kx + n
        k = larger_vector[1] / larger_vector[0]
        n = larger_point[1] - (k * larger_point[0])
        for point in points:
            if k * point[0] + n == point[1]:
                return True
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
        RecursiveDivide(left_cell)
        RecursiveDivide(right_cell)
        
        #and nov ve join both halfes together

        #finding our LR connection
        for left_lr_point in left_cell:
            for right_lr_point in right_cell:
                intersection_found = False
                #check if our new line intersects with anything other connection
                for left_conn in left_cell:
                    for conn in left_conn.connections:
                        if CheckIfIntersects(left_lr_point, right_lr_point, left_conn, conn):
                            intersection_found = True

                for right_conn in right_cell:
                    for conn in right_conn.connections:
                        if CheckIfIntersects(left_lr_point, right_lr_point, right_conn, conn):
                            intersection_found = True

                if not intersection_found:
                    #we found our RL connection
                    break
            if not intersection_found:
                #we break out because found or connection
                break

        print(left_lr_point, right_lr_point, "TO JE LR")
        
        #we nou find left and right candidate for our trianlge (after this step we will complete one triangle)
        #Our LR vector need to change directions so anlges will be correct!
        #left candidate
        all_left_cand = list()
        for left_candidate in left_lr_point.connections:
            if not CheckIfIntersects(left_lr_point, right_lr_point, left_lr_point, left_candidate):
                all_left_cand.append(left_candidate)

        all_right_cand = list()
        #right candidate
        for right_candidate in right_lr_point.connections:
            if not CheckIfIntersects(left_lr_point, right_lr_point, right_lr_point, right_candidate):
                all_right_cand.append(right_candidate)
        
        print(all_left_cand, all_right_cand)
        
        
                
        



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
#for tocka in testne_tocke:
#   print(tocka.connections)

PlotConnectedPoints(testne_tocke)
