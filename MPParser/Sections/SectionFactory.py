from Cities import Cities
from Countries import Countries
from Highways import Highways
from ImgId import ImgId
from Regions import Regions
from POI import Poi
from PolyLine import PolyLine
from Polygon import Polygon


class SectionFactory(object):
    @staticmethod
    def buildSection(fields):
        fieldname = fields[0].lower()
        if fieldname == '[cities]':
            field = Cities(fields, 'Cities')
            field.initAttributes()
            return field
        if fieldname == '[countries]':
            field = Countries(fields, 'Countries')
            field.initAttributes()
            return field
        if fieldname == '[highways]':
            field = Highways(fields, 'Highways')
            field.initAttributes()
            return field
        if fieldname == '[img id]':
            field = ImgId(fields, 'IMG ID')
            field.initAttributes()
            return field
        if fieldname == '[regions]':
            field = Regions(fields, 'Regions')
            field.initAttributes()
            return field
        if fieldname == '[poi]':
            field = Poi(fields, 'POI')
            field.initAttributes()
            return field
        if fieldname == '[polyline]':
            field = PolyLine(fields, 'POLYLINE')
            field.initAttributes()
            return field
        if fieldname == '[polygon]':
            field = Polygon(fields, 'POLYGON')
            field.initAttributes()
            return field
