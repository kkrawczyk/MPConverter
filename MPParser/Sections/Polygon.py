from GeometrySection import GeometrySection
from MPParser.Utils.GeomUtils import GeomUtils


class Polygon(GeometrySection):

    def initAttributes(self):
        super(Polygon, self).initAttributes()
        for k in self.attrs:
            if k.lower().startswith('data'):
                level = k.lower().replace('data', '')
                self.addGeometry(level, GeomUtils.createPolygonFromString(self.attrs[k]))
