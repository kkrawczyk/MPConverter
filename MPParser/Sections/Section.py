from MPParser.Utils.StringUtils import StringUtils

class Section(object):

    def __init__(self, fields, name=''):
        self.fields = fields
        self.name = name
        self.attrs = {}

    def getName(self):
        return self.name

    def addAttribute(self, tag, value, glue=','):
        if tag in self.attrs:
            self.attrs[tag] = self.attrs[tag]+glue+value
        else:
            self.attrs[tag] = value

    def initAttributes(self):
        for i in range(1, len(self.fields)-1):
            tup = StringUtils.split2KeyVal(self.fields[i])
            if len(tup) == 2:
                self.addAttribute(tup[0], tup[1])
            else:
                print 'ERROR: Not a correct tuple: '+tup

    def getAttributes(self):
        return self.attrs

    def printAttributes(self):
        for k in self.attrs:
            print k+' = '+self.attrs[k]

    def init(self):
        pass
