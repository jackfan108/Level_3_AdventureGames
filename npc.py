from person import *
from player import *
import random
import uuid

class NPC (Person):
    npcs = []

    def __init__ (self,name,loc,restlessness,miserly,desc):
        Person.__init__(self,name,loc,desc)
        self._id = uuid.uuid4()
        self._restlessness = restlessness
        self._miserly = miserly
        Clock.clocks[0].register(2,self.move_and_take_stuff,self._id)
        NPC.npcs.append(self)
        
    def move_and_take_stuff (self,time):
        # print (self.name()+" is randomly moving around at " + self.location().name())
        if not self.is_in_limbo():
            if random.randrange(self._restlessness) == 0:
                self.move_somewhere(time)
            if random.randrange(self._miserly) == 0:
                self.take_something(time)

    def move_somewhere (self,time):
        exits = self.location().exits()
        if exits:
            dir = random.choice(exits.keys())
            self.go(dir)

    def take_something (self,time):
        everything = []
        everything.extend(self.stuff_around())
        everything.extend(self.list_contents())
        if everything:
            something = random.choice(everything)
            something.take(self)

    def die (self):
        self.say('SHREEEEEK! I, uh, suddenly feel very faint...')
        Clock.clocks[0].unregister(self._id)
        Person.die(self)