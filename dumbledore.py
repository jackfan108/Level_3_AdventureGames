from player import *
from npc import *
import random
from quest import *

class Wizard (NPC):
    wizards = []
    def __init__ (self,name,loc,restlessness,professorial,desc):
        NPC.__init__(self,name,loc,restlessness,100,desc)
        self._professorial = professorial
        Wizard.wizards.append(self)
        Clock.clocks[0].register(1,self.lecture,self._id)
        Clock.clocks[0].register(1,self.checkTrollBits,self._id)

    _topics = ['Defense Against the Dark Arts',
               'Potions',
               'Charms',
               '2nd Grade Math']

    def lecture (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._professorial) == 0:
            if self.people_around():
                self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
            else:
                self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))

    def checkTrollBits(self,time):
      inventoryNames = []
      for obj in self.contents():
          inventoryNames.append(obj.name())
      if ('Troll Head' in inventoryNames) and ('Troll Bones' in inventoryNames):
        print("Good job! You get 2 points for Gryffindor. Did I say 3? Oops deflation. Suck on that!")
        Quest.quests[0].accomplishQuest()
        sys.exit(0)