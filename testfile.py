import MPParser
from MPParser import ParsingEvent

class SomeKindOfListener(object):
    def onEvent(self, event):
        print event.getEventName()
        print event.getArgs()


lis = SomeKindOfListener()

parser = MPParser.Parser("/home/kkrawczyk/SoftwareSource/ump/tmp/wynik.mp")
parser.addParsingListener(lis)
parser.parse()