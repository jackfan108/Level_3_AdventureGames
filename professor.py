from player import *
from npc import *
import random

class Professor (NPC):

      def __init__ (self,name,loc,restlessness,professorial,desc):
      	  NPC.__init__(self,name,loc,restlessness,100,desc)
          self._professorial = professorial

      _topics = ['Turing machines',
                 'the lambda calculus',
                 'Godel']

      def lecture (self,time):
        if not self.is_in_limbo():
          if random.randrange(self._professorial) == 0:
              if self.people_around():
                  self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
              else:
                  self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))

      def accept (self,obj,source):
        self.say('Thanks, ' + source.name())
        obj.move(self)
        if(obj.is_homework()):
          self.say("Ah, a homework!")
          if (obj.is_done()):
            self.say("I guess you pass.")
            obj.give(self,source)
            if (source.is_player()):
              print("You win, I guess.")
              sys.exit(0)
          else:
            self.say("Take this back.")
            obj.give(self,source)