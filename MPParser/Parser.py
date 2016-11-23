__author__ = 'Krzysztof Krawczyk <k.krawczyk@nova-it.eu>'

class Parser:
    """Class to parse and process MP files"""
    def __init__(self,mpfilename):
        self.mpfilename = mpfilename
        self.isopened = False

    def beforeParsing(self):
        pass
    def afterParsing(self):
        pass
    def processType(self,typename,attributes):
        pass


    def encodeToUtf8(self,text):
        try:
            return unicode(text, "cp1250").encode("UTF-8")
        except:
            return text

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
        self.beforeParsing()
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
                print sectionLines
        self.afterParsing()
        self.close()
