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
        if(self.location() == actor):
          print("You already have it!")
        else:
          print(actor.name() + " takes " + self.name() + " from " + self.location().name())
          if(self.location().is_person()):
            self.location().have_fit()
          self.move(actor)

    def drop(self,actor):
        print(actor.name() + " drops " + self.name() + " in " + actor.location().name())
        self.move(actor.location())

    def give(self,actor,target):
        if(target.is_person()):
          print(actor.name() + " gives " + self.name() + " to " + target.name())
          target.accept(self,actor)
        else:
          print("Who are you giving it to? Is that a person?")