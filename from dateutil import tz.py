from dateutil import tz

class timezone:
    def __init__(self, name):
        self.name = name
        
    
    def getTimezoneDateObject(self):
        timezoneDateObject = tz.gettz(self.name)
        return timezoneDateObject
    