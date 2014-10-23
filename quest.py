from wobject import *
from player import *
from clock import *
import uuid

class Quest(WObject):
    quests = []
    def __init__(self,name,desc):
        self._name = name
        self._desc = desc
        self._done = False
        print(self._desc)
        self._instruction = 'Go find Harry Potter, the troll hunter for further instructions :D'
        print(self._instruction)
        self._id = uuid.uuid4()
        Clock.clocks[0].register(4,self.TrollHunterInRoom,self._id)
        Quest.quests.append(self)


    def TrollHunterInRoom(self,time):
        for people in Player.me.people_around():
            if people.name() == 'Harry-Potter':
                self._instruction = 'You need a powerful weapon... Hmm... Where would you find such a magical object??'
                print self._instruction
                Clock.clocks[0].unregister(self._id)
                Clock.clocks[0].register(1,self.hasTriForce,self._id)


    def hasTriForce(self,time):
        for obj in Player.me.contents():
            if obj.name() == 'trinity-force':
                self._instruction = 'Go slay some fugly trolls... arrr! Collect the head and bones'
                print self._instruction
                Clock.clocks[0].unregister(self._id)
                Clock.clocks[0].register(1,self.hasTrollBits,self._id)


    def hasTrollBits(self,time):
        inventoryNames = []
        for obj in Player.me.contents():
            inventoryNames.append(obj.name())
        if ('Troll-Head' in inventoryNames) and ('Troll-Bones' in inventoryNames):
            self._instruction = 'Return to Dumbledore and hand in your troll bits for a troll-hunting diploma and 3 points for Gryffindor.'
            print self._instruction
            Clock.clocks[0].unregister(self._id)

    def accomplishQuest(self):
        self._done = True
        print "You've completed the quest!"
        self.destroy()
