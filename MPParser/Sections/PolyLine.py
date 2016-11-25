from GeometrySection import GeometrySection
from MPParser.Utils.GeomUtils import GeomUtils


class PolyLine(GeometrySection):

    def initAttributes(self):
        super(PolyLine, self).initAttributes()
        for k in self.attrs:
            if k.lower().startswith('data'):
                level = k.lower().replace('data', '')
                self.addGeometry(level, GeomUtils.createPolylineFromString(self.attrs[k]))
