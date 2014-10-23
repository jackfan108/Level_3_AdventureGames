from mobile import *
from room import *


class Weapon (MobileThing):

    def __init__ (self,name,loc,damage,attack_desc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._damage = damage
        self._attack_desc = attack_desc

    def use (self,actor):
        people = actor.people_around()
        for person in people:
          if person.is_troll():
            actor.say('I use the power of ' + self.name() + " to strike down " + person.name() + "!")
            actor.location().report(self._attack_desc)
            person.suffer(self._damage)