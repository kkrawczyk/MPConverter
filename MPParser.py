__author__ = 'Krzysztof Krawczyk <k.krawczyk@nova-it.eu>'

class MPParser:
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
        for line in self.filehandler:
            linenum+=1
            line = line.strip()
            if line == "[POLYLINE]":
                type = "POLYLINE"
                attributes = {}
                attributes['linenum']=linenum
            elif line == "[POLYGON]":
                type = "POLYGON"
                attributes = {}
                attributes['linenum']=linenum
            elif line == "[POI]":
                type = "POI"
                attributes = {}
                attributes['linenum']=linenum
            elif line == "[IMG ID]":
                type = "IMG_ID"
                attributes = {}
                attributes['linenum']=linenum
            elif line == '[END]' or line == '[END-IMG ID]':
                self.processType(type,attributes)
                type = None
                attributes = None
            elif line.startswith(';'):
                pass
            elif attributes is not None and line != '':
                if line.startswith("["):
                    pass
                else:
                    try:
                        key,v = line.split('=', 1)
                        key = key.strip()
                        if key in attributes:
                            if key.startswith('Data'):
                                key = "_Inner0"
                                while key in attributes:
                                    key = "_Inner" + str(int(key[6:]) + 1)
                            elif key == 'City' and attributes[key] == 'Y':
                                pass
                            elif key.startswith("RegionIdx"):
                                pass
                            else:
                                raise ParsingError('Key ' + key + ' repeats')
                        attributes[key]=self.encodeToUtf8(v).strip()
                    except ParsingError as e:
                        raise ParsingError('Can\'t split the thing: '+line+" "+e.message)
        print linenum
        self.afterParsing()
        self.close()



class ParsingError(Exception):
        pass