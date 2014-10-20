from npc import *
from homework import *

class Badninja(NPC):
  badninjas = []
  def __init__ (self,name,loc,restlessness,desc):
    NPC.__init__(self,name,loc,restlessness,10,desc)
    Clock.clocks[0].register(1,self.steal_homework,self._id)
    Badninja.badninjas.append(self)

  def steal_homework (self,time):
    if not self.is_in_limbo():
        everything = []
        everything.extend(self.stuff_around())
        everything.extend(self.list_contents())
        if everything:
          for thing in everything:
            if (thing.is_homework()):
              if (thing.is_done()):
                thing.take(self)
                self.say('I HATE HOMEWORK!!')
                thing.destroy()