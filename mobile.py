from thing import *

class MobileThing (Thing):
    instances = []

    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)
        self._original_location = loc
        MobileThing.instances.append(self)


    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self) 
        self._location = loc

    def creation_site (self):
        return self._original_location

    def is_mobile_thing (self):
        return True

    def take(self,actor):
        self.move(actor)

    def drop(self,actor):
        self.move(actor.location())

    def give(self,actor,target):
        self.move(target)
