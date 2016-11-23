import MPParser_old

__author__ = 'Krzysztof Krawczyk'

class MP2OSM(MPParser_old.MPParser):
    def __init__(self,mpfilename):
        MPParser_old.MPParser.__init__(self, mpfilename)
        self.ignoredKeys = []

    def processNodes(self,nodes_str,typename):
        nodes = []
        for element in nodes_str.split(','):
            element = element.strip('()')
            nodes.append(element)
        lats = []
        longs = []
        for la in nodes[::2]:
            l=len(la)
            if l < 9:
                la += '0'*(9-l)
            lats.append(la)
        for lo in nodes[1::2]:
            l=len(lo)
            if l < 9:
                lo += '0'*(9-l)
            longs.append(lo)
        nodes = zip(lats, longs)
        print nodes
        #for node in nodes:
        #    if node not in points:
        #        points_append(node, {})


    def prepareAttributes(self,typename,attributes):
        attrs = {}
        for key in attributes:
            value = attributes[key]
            if key.lower() == 'label':
                key = 'name'
                attrs[key]=value
            elif key.lower() == 'typ':
                key = 'ump:typ'
                attrs[key]=value
            elif key.lower() == 'label3':
                key = 'loc_name'
                attrs[key]=value
            elif key == 'DirIndicator':
                key = 'oneway'
                attrs[key]=value
            elif key in [ 'Data0', 'Data1', 'Data2', 'Data3', 'Data4' ]:
                num = int(key[4:])
                self.processNodes(value,typename)


        return attrs
    def processType(self,typename,attributes):
        self.prepareAttributes(typename,attributes)
