from mobile import *
from random import randint
import uuid
from clock import *
from butterfly import *

class Caterpillar (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._id = uuid.uuid4()
        Clock.clocks[0].register(2,self.transform,self._id)
        self._isCocoon = False
        self._t1 = randint(1,4)
        self._t2 = randint(5,8)

    def is_Cocoon (self):
        return self._isCocoon

    def is_Caterpillar (self):
        return not self._isCocoon

    def transform (self, time):
        if time == self._t1:
            self._isCocoon = True
            self._name = 'cocoon'
            if self.location().is_person():
                self.location().location().report('Something funny is happening to the caterpillar...')
            else:
                self.location().report('Something funny is happening to the caterpillar...')
            self.desc = 'I\'m all wrapped up as a cocoon :D'
        if time == self._t2:
            if self.location().is_person():
                self.location().location().report('A butterfly bursts out of the cocoon. I\'m freeeeeeeeeee...')
                Butterfly('butterfly', self._location.location(), 1, 'it\'s a beautiful butterfly.')
            else:
                self.location().report('A butterfly bursts out of the cocoon. I\'m freeeeeeeeeee...')
                Butterfly('butterfly', self._location, 1, 'it\'s a beautiful butterfly.')
            self.destroy()