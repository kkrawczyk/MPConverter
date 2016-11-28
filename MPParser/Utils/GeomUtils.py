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
        return Point(t[1], t[0])

    @staticmethod
    def createPolylineFromString(data):
        if not data.startswith('['):
            data = '['+data+']'
        t = eval(data)
        t2 = []
        for p in t:
            p2 = [p[1], p[0]]
            t2.append(p2)
        return LineString(t2)

    @staticmethod
    def createPolygonFromString(data):
        if not data.startswith('['):
            data = '['+data+']'
        t = eval(data)
        t2 = []
        for p in t:
            p2 = [p[1], p[0]]
            t2.append(p2)
        return Polygon(t2)
