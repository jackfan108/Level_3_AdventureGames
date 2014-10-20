from player import *
from npc import *
from troll import *

class Trollhunter(NPC):

  def __init__ (self,name,loc,restlessness,desc):
    NPC.__init__(self,name,loc,restlessness,10,desc)
    
  def look_for_trolls (self,time):
    if not self.is_in_limbo():
      people = self.people_around()
      for target in people:
        if (target.is_troll()):
          self.say('A troll! ATTAAAAAACK!')
          self.location().report(self.name() + ' attaacks the troll ' + target.name())
          target.suffer(999)