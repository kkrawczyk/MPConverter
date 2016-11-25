from ast import literal_eval as make_tuple

from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon

class GeomUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def createPointFromString(text):
        t = make_tuple(text)
        return Point(t[0], t[1])

    @staticmethod
    def createPolylineFromString(data):
        if not data.startswith('['):
            data = '['+data+']'
        t = eval(data)
        return LineString(t)

    @staticmethod
    def createPolygonFromString(data):
        if not data.startswith('['):
            data = '['+data+']'
        t = eval(data)
        return Polygon(t)
