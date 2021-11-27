from globals import *

class Ship():
    def __init__(self, arrivalTime, id = 0):
        self.timeout = 0
        self.timeInPort = 0
        self.timeOnDock = 0
        self.timeArrivalAtPier = 0
        self.timeArrivalAtPort = arrivalTime
        self.type = type_generator()
        self.loadTime = load_time_generator(self.type)
        self.id = id
    
    def __lt__(self,other):
        if self.id < other.id:
            return True
        return False

class Pier():
    def __init__(self):
        self.endLoad  = 0
        self.ship = None

class Tugboat():
    def __init__(self):
        self.location = "Puerto"
