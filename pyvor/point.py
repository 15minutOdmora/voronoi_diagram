class Point:
    """
    class for points
    """

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._connections = list()

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
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    
    def AddConnection(self, point):
        """
        Adds point to connections
        """
        self._connections.append(point)

    

