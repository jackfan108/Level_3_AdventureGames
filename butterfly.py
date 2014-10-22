from person import *
import uuid
from clock import *
import random

class Butterfly (Person):
    butterflies = []

    def __init__ (self,name,loc,restlessness,desc):
        Person.__init__(self,name,loc,desc)
        self._id = uuid.uuid4()
        self._restlessness = restlessness
        Clock.clocks[0].register(2,self.move_somewhere,self._id)
        Butterfly.butterflies.append(self)

    def move_somewhere (self,time):
        if not self.is_in_limbo():
            if random.randrange(self._restlessness) == 0:
                exits = self.location().exits()
                if exits:
                    dir = random.choice(exits.keys())
                    self.go(dir)

    def suffer (self,hits):
        self.say('That was really mean!')