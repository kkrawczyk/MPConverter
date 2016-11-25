from GeometrySection import GeometrySection
from MPParser.Utils.GeomUtils import GeomUtils


class Poi(GeometrySection):

    def initAttributes(self):
        super(Poi, self).initAttributes()
        for k in self.attrs:
            if k.lower().startswith('data'):
                level = k.lower().replace('data', '')
                self.addGeometry(level,GeomUtils.createPointFromString(self.attrs[k]))
