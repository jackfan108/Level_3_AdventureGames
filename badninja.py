from player import *
from npc import *
from homework import *

class Badninja(NPC):

  def __init__ (self,name,loc,restlessness,desc):
    NPC.__init__(self,name,loc,restlessness,10,desc)
    
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