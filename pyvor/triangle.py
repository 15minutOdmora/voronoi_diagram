class Triangle:
    """
    Razred, v katerem bomo hranili trikotnike oziroma njegove tri tocke
    """
    def __init__(self, points):
        """
        """
        self._points = points
    
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        if len(value) != 3:
            raise ValueError("Invalid number of points")
        self._points = value
