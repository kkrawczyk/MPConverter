from __builtin__ import callable

from Sections.SectionFactory import SectionFactory
from ParsingEvent import ParsingEvent
from ParsingListener import ParsingListener

from Sections.Cities import Cities
from Sections.Countries import Countries
from Sections.Highways import Highways
from Sections.ImgId import ImgId
from Sections.Regions import Regions
from Sections.POI import Poi
from Sections.PolyLine import PolyLine
from Sections.Polygon import Polygon

__author__ = 'Krzysztof Krawczyk <k.krawczyk@nova-it.eu>'


class Parser(object):
    """Class to parse and process MP files"""
    def __init__(self,mpfilename):
        self.mpfilename = mpfilename
        self.isopened = False
        self.parsingListeners = []

    def notifyParsingListeners(self, event):
        for pl in self.parsingListeners:
            if isinstance(pl, ParsingListener):
                pl.onEvent(event)
            else:
                op = getattr(pl, "onEvent", event)
                if callable(op):
                    op(event)

    def addParsingListener(self, listener):
        self.parsingListeners.append(listener)

    def open(self):
        self.filehandler = open(self.mpfilename,'r')
        self.isopened = True

    def close(self):
        if self.isopened==True:
            self.filehandler.close()
            self.isopened = False


    def parse(self):
        if self.isopened==False:
            self.open()
        self.notifyParsingListeners(ParsingEvent("PARSING_START"))
        type = None
        attributes = None
        linenum = 0
        sectionLines = []
        inSection = False
        for line in self.filehandler:
            linenum+=1
            line = line.strip()
            if line.startswith('[') and not line.startswith('[END'):
                inSection=True
                sectionLines = []
            sectionLines.append(line)
            if line.startswith('[END'):
                inSection=False
                sec = SectionFactory.buildSection(sectionLines)
                self.notifyParsingListeners(ParsingEvent("PARSED_SECTION", {'section': sec}))
                if not sec:
                    print sectionLines[0]
                #if sec and not isinstance(sec, Cities) and not isinstance(sec, Countries) and not isinstance(sec, Highways) and not isinstance(sec, ImgId) and not isinstance(sec, Regions) and not isinstance(sec, Poi) and not isinstance(sec, PolyLine) and not isinstance(sec, Polygon):
                #    sec.printAttributes()
                #else:
                #    print sectionLines[0]
        self.notifyParsingListeners(ParsingEvent("PARSING_END"))
        self.close()
