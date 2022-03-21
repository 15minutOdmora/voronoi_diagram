class Point:
    """
    class for points
    """

    def __init__(self, x, y, connections=list()):
        self._x = x
        self._y = y
        self._connections = connections

    #getters and setters
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("Negative value")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("Negative value")
        self._y = value

    @property
    def connections(self):
        return self._connections

    @connections.setter
    def connections(self, value):
        self._connections = value

    
    def AddConnection(self, point):
        """
        Adds point to connections
        """
        self._connections.append(point)

    

