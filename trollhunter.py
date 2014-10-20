from player import *
from npc import *
from troll import *

class Trollhunter(NPC):
  trollhunters = []
  def __init__ (self,name,loc,restlessness,desc):
    NPC.__init__(self,name,loc,restlessness,10,desc)
    Trollhunter.trollhunters.append(self)
    Clock.clocks[0].register(1,self.look_for_trolls,self._id)
    
  def look_for_trolls (self,time):
    if not self.is_in_limbo():
      people = self.people_around()
      for target in people:
        if (target.is_troll()):
          self.say('A troll! ATTAAAAAACK!')
          self.location().report(self.name() + ' attaacks the troll ' + target.name())
          target.suffer(999)