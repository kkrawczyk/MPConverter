from Section import Section


class GeometrySection(Section):
    def __init__(self, fields, name):
        super(GeometrySection, self).__init__(fields, name)
        self.geometries = {}

    def getGeometry(self, level):
        if self.geometries.has_key(level):
            return self.geometries[level]
        else:
            raise Exception("Problem with geometry!!")

    def getGeometries(self):
        return self.geometries

    def addGeometry(self,level, geom):
        self.geometries[level] = geom
