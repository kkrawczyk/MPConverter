class ParsingEvent(object):

    def __init__(self, eventName, args = None):
        self.eventName = eventName
        self.args = {}
        if args:
            for k in args:
                self.args[k]=args[k]

    def getEventName(self):
        return self.eventName

    def getArgs(self):
        return self.args
