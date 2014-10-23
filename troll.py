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

    def die (self):
        self.location().broadcast('An earth-shattering, soul-piercing scream is heard...')
        item = random.randint(1,3)
        if item == 1:
            MobileThing('Troll-Head',self.location(),'This is the head of a troll...')
        elif item == 2:
            MobileThing('Troll-Bones',self.location(),'These are the bones of a troll...')
        else:
            self.say('Better luck next time! No troll bits for you!')
        self.destroy()