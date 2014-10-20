import random
from npc import *
from player import *
from person import *

class Troll (NPC):
    trolls = []

    def __init__ (self,name,loc,restlessness,hunger,desc):
        NPC.__init__(self,name,loc,restlessness,10,desc)
        self._hunger = hunger
        Troll.trolls.append(self)
        Clock.clocks[0].register(1,self.eat_people,self._id)

    def eat_people (self,time):
        if not self.is_in_limbo():
            if random.randrange(self._hunger) == 0:
                people = self.people_around()
                print 'numnumnum'
                if people:
                    victim = random.choice(people)
                    self.location().report(self.name() + ' takes a bite out of ' + victim.name())
                    victim.suffer(random.randint(1,3))
                else:
                    self.location().report(self.name() + "'s belly rumbles")

    def is_troll (self):
      return True